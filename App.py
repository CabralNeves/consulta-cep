import streamlit as st
import requests
import pandas as pd
from time import sleep

# Configuração inicial da página
st.set_page_config(
    page_title="Consulta CEP",
    page_icon="📍",
    layout="centered"
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

# Função para consultar CEP
def consultar_cep(cep):
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
st.title("🏠 Consulta de CEP")
st.markdown("### Encontre endereços facilmente!")

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
                # Card com os resultados
                st.success("CEP encontrado!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### 📍 Localização")
                    st.write(f"**CEP:** {dados.get('cep', '')}")
                    st.write(f"**Cidade:** {dados.get('localidade', '')}")
                    st.write(f"**Estado:** {dados.get('uf', '')}")
                    st.write(f"**DDD:** {dados.get('ddd', '')}")
                
                with col2:
                    st.markdown("#### 🏣 Endereço")
                    st.write(f"**Logradouro:** {dados.get('logradouro', '')}")
                    st.write(f"**Bairro:** {dados.get('bairro', '')}")
                    st.write(f"**Complemento:** {dados.get('complemento', '') or 'N/A'}")
                
                # Botão para copiar endereço completo
                endereco_completo = f"{dados.get('logradouro', '')}, {dados.get('bairro', '')}, {dados.get('localidade', '')}-{dados.get('uf', '')}, CEP: {dados.get('cep', '')}"
                if st.button("📋 Copiar endereço completo"):
                    st.code(endereco_completo)
                    st.toast("Endereço copiado!", icon="✅")

# Informações adicionais
with st.expander("ℹ️ Sobre"):
    st.markdown("""
        **Como usar:**
        1. Digite o CEP desejado no campo de busca
        2. Clique em "Buscar" ou pressione Enter
        3. Os dados do endereço serão exibidos abaixo
        
        **Observações:**
        - O CEP pode ser digitado com ou sem hífen
        - Todos os dados são obtidos através da API ViaCEP
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; padding: 1rem;'>"
    "Desenvolvido com  usando Streamlit - Por: NevesX - Tech & Soluções Digitais"
    "</div>",
    unsafe_allow_html=True
)