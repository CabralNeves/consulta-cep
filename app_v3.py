import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time
import io

# Configuração da página
st.set_page_config(
    page_title="Consulta Multi-CEP",
    page_icon="📍",
    layout="wide"
)

# Estilo CSS personalizado
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stAlert {
        padding: 1rem;
        border-radius: 0.5rem;
    }
    div[data-testid="stForm"] {
        border: 1px solid #ddd;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

def get_location_coordinates(address):
    """Função para obter coordenadas de um endereço"""
    try:
        geolocator = Nominatim(user_agent="multi_cep_app")
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        return None
    except GeocoderTimedOut:
        return None

def create_map(locations):
    """Função para criar mapa com múltiplos pontos"""
    if not locations:
        return None
        
    # Encontra o centro médio dos pontos
    center_lat = sum(loc['lat'] for loc in locations) / len(locations)
    center_lon = sum(loc['lon'] for loc in locations) / len(locations)
    
    m = folium.Map(location=[center_lat, center_lon], zoom_start=12)
    
    # Adiciona marcadores para cada localização
    for loc in locations:
        folium.Marker(
            [loc['lat'], loc['lon']],
            popup=loc['address'],
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
    
    return m

def consultar_cep(cep):
    """Função para consultar um único CEP"""
    cep = ''.join(filter(str.isdigit, str(cep)))
    if len(cep) != 8:
        return None, "CEP deve conter 8 dígitos"
    
    try:
        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        
        if "erro" in dados:
            return None, "CEP não encontrado"
            
        return dados, None
        
    except requests.exceptions.RequestException as e:
        return None, f"Erro na consulta: {str(e)}"

def processar_ceps(ceps):
    """Função para processar múltiplos CEPs"""
    resultados = []
    locations = []
    erros = []
    
    with st.spinner('Consultando CEPs...'):
        progress_bar = st.progress(0)
        total = len(ceps)
        
        for i, cep in enumerate(ceps):
            dados, erro = consultar_cep(cep)
            if dados:
                resultados.append(dados)
                endereco = f"{dados.get('logradouro', '')}, {dados.get('bairro', '')}, {dados.get('localidade', '')}-{dados.get('uf', '')}"
                coords = get_location_coordinates(endereco)
                if coords:
                    locations.append({
                        'lat': coords[0],
                        'lon': coords[1],
                        'address': endereco
                    })
            else:
                erros.append(f"CEP {cep}: {erro}")
            
            progress_bar.progress((i + 1) / total)
            time.sleep(0.5)  # Delay para evitar sobrecarga na API
            
        progress_bar.empty()
            
    return resultados, locations, erros

def processar_excel(df):
    """Função para processar DataFrame do Excel"""
    # Tentar encontrar coluna de CEP
    possiveis_colunas_cep = ['cep', 'CEP', 'Cep', 'código postal', 'codigo postal', 'postal']
    coluna_cep = None
    
    # Procurar por colunas que podem conter CEP
    for col in df.columns:
        if str(col).lower() in possiveis_colunas_cep:
            coluna_cep = col
            break
    
    if coluna_cep is None:
        # Se não encontrou, mostrar seletor de coluna
        coluna_cep = st.selectbox(
            "Selecione a coluna que contém os CEPs:",
            options=df.columns
        )
    
    # Extrair CEPs únicos e válidos
    ceps = df[coluna_cep].dropna().unique()
    ceps = [str(cep).strip() for cep in ceps]
    return ceps

# Interface principal
st.title("🏠 Consulta Multi-CEP")
st.markdown("### Consulte múltiplos CEPs de uma vez!")

# Tabs para diferentes modos de entrada
tab1, tab2 = st.tabs(["Digite os CEPs", "Upload de Arquivo"])

with tab1:
    ceps_input = st.text_area(
        "Digite os CEPs (um por linha)",
        height=150,
        help="Digite um CEP por linha, com ou sem hífen"
    )
    if st.button("🔍 Consultar CEPs", key="consulta_manual"):
        if ceps_input.strip():
            ceps = [cep.strip() for cep in ceps_input.split('\n') if cep.strip()]
            resultados, locations, erros = processar_ceps(ceps)
        else:
            st.warning("Por favor, digite pelo menos um CEP.")

with tab2:
    uploaded_file = st.file_uploader(
        "Escolha um arquivo Excel ou TXT com os CEPs",
        type=['xlsx', 'xls', 'txt']
    )
    if uploaded_file:
        if uploaded_file.type in ['application/vnd.ms-excel', 
                                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']:
            try:
                df = pd.read_excel(uploaded_file)
                ceps = processar_excel(df)
                if st.button("📂 Processar Arquivo", key="consulta_arquivo"):
                    resultados, locations, erros = processar_ceps(ceps)
            except Exception as e:
                st.error(f"Erro ao ler arquivo Excel: {str(e)}")
        else:  # arquivo TXT
            if st.button("📂 Processar Arquivo", key="consulta_arquivo"):
                content = uploaded_file.read().decode()
                ceps = [line.strip() for line in content.split('\n') if line.strip()]
                resultados, locations, erros = processar_ceps(ceps)

# Exibição dos resultados
if 'resultados' in locals() and resultados:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.success(f"{len(resultados)} CEPs encontrados!")
        
        # Criar DataFrame para exibição
        df_resultados = pd.DataFrame(resultados)
        st.dataframe(df_resultados)
        
        # Botões para download
        col_download1, col_download2 = st.columns(2)
        
        with col_download1:
            # Download CSV
            csv = df_resultados.to_csv(index=False)
            st.download_button(
                "📥 Download CSV",
                csv,
                "resultados_cep.csv",
                "text/csv",
                key='download-csv'
            )
            
        with col_download2:
            # Download Excel
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df_resultados.to_excel(writer, sheet_name='Resultados', index=False)
            excel_data = output.getvalue()
            st.download_button(
                "📥 Download Excel",
                excel_data,
                "resultados_cep.xlsx",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key='download-excel'
            )
    
    with col2:
        if locations:
            st.markdown("#### 🗺️ Localização no Mapa")
            mapa = create_map(locations)
            if mapa:
                folium_static(mapa, width=800)
        else:
            st.warning("Não foi possível gerar o mapa para os endereços.")
            
    # Exibir erros, se houver
    if erros:
        st.error("Alguns CEPs não puderam ser processados:")
        for erro in erros:
            st.write(erro)

# Informações adicionais
with st.expander("ℹ️ Como usar"):
    st.markdown("""
        **Opções de uso:**
        1. Digite os CEPs manualmente na primeira aba (um por linha)
        2. Faça upload de um arquivo Excel ou TXT na segunda aba
        
        **Formatos aceitos:**
        - Excel (.xlsx, .xls)
        - Arquivo de texto (.txt)
        
        **Para arquivos Excel:**
        - O sistema tentará identificar automaticamente a coluna de CEPs
        - Caso não identifique, você poderá selecionar a coluna correta
        
        **Resultados:**
        - Visualização em tabela
        - Mapa interativo com todos os endereços
        - Download em CSV ou Excel
        - Lista de erros (se houver)
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; padding: 1rem;'>"
    "Desenvolvido com usando Python e Streamlit - Por: NevesX - Tech & Soluções Digitais"
    "</div>",
    unsafe_allow_html=True
)