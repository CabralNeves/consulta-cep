import streamlit as st
import requests
import pandas as pd
from time import sleep
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Configuração inicial da página
st.set_page_config(
    page_title="Consulta CEP 2.0",
    page_icon="📍",
    layout="wide"  # Mudamos para wide para acomodar o mapa
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
    """Função para obter coordenadas de um endereço usando Nominatim"""
    try:
        geolocator = Nominatim(user_agent="consulta_cep_app")
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        return None
    except GeocoderTimedOut:
        return None

def create_map(lat, lon, address):
    """Função para criar o mapa com Folium"""
    m = folium.Map(location=[lat, lon], zoom_start=15)
    
    # Adiciona marcador
    folium.Marker(
        [lat, lon],
        popup=address,
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)
    
    # Adiciona círculo da região
    folium.Circle(
        radius=500,  # 500 metros de raio
        location=[lat, lon],
        color='blue',
        fill=True,
    ).add_to(m)
    
    return m

def consultar_cep(cep):
    """Função para consultar CEP"""
    cep = ''.join(filter(str.isdigit, cep))
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
        
    except requests.exceptions.HTTPError:
        return None, "Erro ao consultar o serviço de CEP"
    except requests.exceptions.ConnectionError:
        return None, "Erro de conexão. Verifique sua internet."
    except Exception as e:
        return None, f"Erro inesperado: {str(e)}"

# Título principal com emoji
st.title("🏠 Consulta de CEP 2.0")
st.markdown("### Encontre endereços facilmente com visualização no mapa!")

# Container principal
with st.container():
    # Formulário de pesquisa
    with st.form("form_consulta"):
        col1, col2 = st.columns([3, 1])
        with col1:
            cep_input = st.text_input(
                "Digite o CEP",
                placeholder="Ex: 60060-390",
                help="Digite o CEP com ou sem hífen"
            )
        with col2:
            submit_button = st.form_submit_button("🔍 Buscar")

    # Processamento da consulta
    if submit_button and cep_input:
        with st.spinner('Consultando CEP...'):
            sleep(0.5)  # Pequeno delay para melhor UX
            dados, erro = consultar_cep(cep_input)
            
            if erro:
                st.error(erro)
            else:
                # Criando layout com duas colunas
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    # Card com os resultados
                    st.success("CEP encontrado!")
                    
                    st.markdown("#### 📍 Localização")
                    st.write(f"**CEP:** {dados.get('cep', '')}")
                    st.write(f"**Cidade:** {dados.get('localidade', '')}")
                    st.write(f"**Estado:** {dados.get('uf', '')}")
                    st.write(f"**DDD:** {dados.get('ddd', '')}")
                    
                    st.markdown("#### 🏣 Endereço")
                    st.write(f"**Logradouro:** {dados.get('logradouro', '')}")
                    st.write(f"**Bairro:** {dados.get('bairro', '')}")
                    st.write(f"**Complemento:** {dados.get('complemento', '') or 'N/A'}")
                    
                    # Botão para copiar endereço completo
                    endereco_completo = f"{dados.get('logradouro', '')}, {dados.get('bairro', '')}, {dados.get('localidade', '')}-{dados.get('uf', '')}, CEP: {dados.get('cep', '')}"
                    if st.button("📋 Copiar endereço completo"):
                        st.code(endereco_completo)
                        st.toast("Endereço copiado!", icon="✅")
                
                with col2:
                    # Mapa
                    st.markdown("#### 🗺️ Localização no Mapa")
                    
                    # Obtém coordenadas do endereço
                    endereco_mapa = f"{dados.get('logradouro', '')}, {dados.get('bairro', '')}, {dados.get('localidade', '')}, {dados.get('uf', '')}"
                    coords = get_location_coordinates(endereco_mapa)
                    
                    if coords:
                        lat, lon = coords
                        mapa = create_map(lat, lon, endereco_mapa)
                        folium_static(mapa, width=600)
                    else:
                        st.warning("Não foi possível carregar o mapa para este endereço.")

# Informações adicionais
with st.expander("ℹ️ Sobre"):
    st.markdown("""
        **Como usar:**
        1. Digite o CEP desejado no campo de busca
        2. Clique em "Buscar" ou pressione Enter
        3. Os dados do endereço serão exibidos à esquerda
        4. O mapa da região será mostrado à direita
        
        **Observações:**
        - O CEP pode ser digitado com ou sem hífen
        - O mapa mostra um raio de 500 metros da localização
        - Todos os dados são obtidos através da API ViaCEP e OpenStreetMap
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; padding: 1rem;'>"
    "Desenvolvido com usando Streamlit - Por: NevesX - Tech & Soluções Digitais"
    "</div>",
    unsafe_allow_html=True
)