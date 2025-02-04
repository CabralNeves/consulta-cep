<<<<<<< HEAD
# Documentação Técnica - Consulta Multi-CEP v3.0

## Sumário
1. [Visão Geral](#visão-geral)
2. [Arquitetura](#arquitetura)
3. [Instalação](#instalação)
4. [Configuração](#configuração)
5. [Funcionalidades](#funcionalidades)
6. [API e Integrações](#api-e-integrações)
7. [Processamento de Dados](#processamento-de-dados)
8. [Interface do Usuário](#interface-do-usuário)
9. [Deployment](#deployment)
10. [Troubleshooting](#troubleshooting)

## Visão Geral
Sistema de consulta múltipla de CEPs com suporte a diferentes formatos de entrada e visualização geográfica.

### Principais Componentes
- Interface web interativa
- Processador de arquivos Excel/TXT
- Sistema de geocodificação
- Visualização em mapa
- Exportação de dados

## Arquitetura

```
Consulta Multi-CEP
├── Frontend (Streamlit)
│   ├── Interface do Usuário
│   ├── Mapa Interativo (Folium)
│   └── Processamento de Arquivos
├── Backend (Python)
│   ├── Processamento de CEP
│   ├── Geocodificação
│   ├── Manipulação de Excel
│   └── Validações
└── APIs Externas
    ├── ViaCEP
    └── OpenStreetMap
```

## Instalação

### Requisitos do Sistema
- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)
- Acesso à internet

### Dependências Principais
```text
streamlit==1.31.1
requests==2.31.0
pandas==2.2.0
folium==0.15.1
geopy==2.4.1
openpyxl==3.1.2
xlsxwriter==3.1.9
```

### Instalação Passo a Passo
```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/consulta-cep.git

# 2. Entre no diretório
cd consulta-cep

# 3. Crie um ambiente virtual
python -m venv venv

# 4. Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 5. Instale as dependências
pip install -r requirements.txt
```

## Funcionalidades

### 1. Processamento de Entrada
- **Entrada Manual**
  - Suporte a múltiplos CEPs
  - Validação de formato
  - Remoção de duplicatas

- **Upload de Arquivo**
  - Suporte a Excel (.xlsx, .xls)
  - Suporte a TXT
  - Detecção automática de coluna

### 2. Consulta de CEP
- Processamento em lote
- Tratamento de erros individual
- Feedback em tempo real
- Sistema anti-sobrecarga

### 3. Geocodificação
- Conversão de endereços em coordenadas
- Suporte a múltiplos pontos
- Tratamento de erros de localização

### 4. Visualização
- Mapa interativo
- Múltiplos marcadores
- Popup com informações
- Zoom automático

### 5. Exportação
- Formato CSV
- Formato Excel
- Dados formatados
- Seleção de colunas

## API e Integrações

### ViaCEP
```python
def consultar_cep(cep: str) -> tuple[dict, str]:
    """
    Consulta um CEP na API ViaCEP.
    
    Args:
        cep: string contendo o CEP
        
    Returns:
        tuple: (dados do endereço, mensagem de erro)
    """
```

### Geocodificação
```python
def get_location_coordinates(address: str) -> tuple[float, float]:
    """
    Obtém coordenadas de um endereço usando Nominatim.
    
    Args:
        address: string contendo o endereço completo
        
    Returns:
        tuple: (latitude, longitude)
    """
```

## Processamento de Dados

### Excel
```python
def processar_excel(df: pd.DataFrame) -> list:
    """
    Processa DataFrame do Excel para extrair CEPs.
    
    Args:
        df: DataFrame contendo os dados
        
    Returns:
        list: Lista de CEPs únicos
    """
```

### Validações
- Formato do CEP
- Existência do CEP
- Formato do arquivo
- Dados obrigatórios

## Interface do Usuário

### Componentes
- Tabs de navegação
- Área de upload
- Barra de progresso
- Mapa interativo
- Tabela de resultados
- Botões de download

### Feedback Visual
- Mensagens de sucesso/erro
- Indicador de progresso
- Tooltips informativos
- Validações em tempo real

## Deployment

### Requisitos de Servidor
- Python 3.9+
- 2GB RAM mínimo
- Acesso à internet
- Permissões de escrita

### Configuração
```bash
# Instalação de dependências
pip install -r requirements.txt

# Execução
streamlit run app_v3.py --server.port=8501
```

### Variáveis de Ambiente
```env
DEBUG=False
PORT=8501
CACHE_TTL=3600
```

## Troubleshooting

### Problemas Comuns

1. **Erro na leitura do Excel**
```python
# Verifique o formato do arquivo
# Use modo de compatibilidade
df = pd.read_excel(file, engine='openpyxl')
```

2. **Falha na Geocodificação**
- Verifique conexão com internet
- Implemente retry
- Use cache local

3. **Memória Insuficiente**
- Processe em lotes
- Limpe cache periodicamente
- Otimize dataframes

### Logs e Monitoramento
- Logs de erro detalhados
- Métricas de uso
- Tempo de processamento
- Taxa de sucesso

### Manutenção
- Atualizações regulares
- Backup de dados
- Limpeza de cache
- Monitoramento de API

---

## 📝 Changelog

### [3.0.0] - 2024-02-02
#### Adicionado
- Suporte a Excel
- Multi-consulta
- Mapa interativo
- Download de resultados
- Barra de progresso

#### Modificado
- Interface reformulada
- Processamento otimizado
- Sistema de feedback
- Tratamento de erros

---

=======
# Documentação Técnica - Consulta Multi-CEP v3.0

## Sumário
1. [Visão Geral](#visão-geral)
2. [Arquitetura](#arquitetura)
3. [Instalação](#instalação)
4. [Configuração](#configuração)
5. [Funcionalidades](#funcionalidades)
6. [API e Integrações](#api-e-integrações)
7. [Processamento de Dados](#processamento-de-dados)
8. [Interface do Usuário](#interface-do-usuário)
9. [Deployment](#deployment)
10. [Troubleshooting](#troubleshooting)

## Visão Geral
Sistema de consulta múltipla de CEPs com suporte a diferentes formatos de entrada e visualização geográfica.

### Principais Componentes
- Interface web interativa
- Processador de arquivos Excel/TXT
- Sistema de geocodificação
- Visualização em mapa
- Exportação de dados

## Arquitetura

```
Consulta Multi-CEP
├── Frontend (Streamlit)
│   ├── Interface do Usuário
│   ├── Mapa Interativo (Folium)
│   └── Processamento de Arquivos
├── Backend (Python)
│   ├── Processamento de CEP
│   ├── Geocodificação
│   ├── Manipulação de Excel
│   └── Validações
└── APIs Externas
    ├── ViaCEP
    └── OpenStreetMap
```

## Instalação

### Requisitos do Sistema
- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)
- Acesso à internet

### Dependências Principais
```text
streamlit==1.31.1
requests==2.31.0
pandas==2.2.0
folium==0.15.1
geopy==2.4.1
openpyxl==3.1.2
xlsxwriter==3.1.9
```

### Instalação Passo a Passo
```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/consulta-cep.git

# 2. Entre no diretório
cd consulta-cep

# 3. Crie um ambiente virtual
python -m venv venv

# 4. Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 5. Instale as dependências
pip install -r requirements.txt
```

## Funcionalidades

### 1. Processamento de Entrada
- **Entrada Manual**
  - Suporte a múltiplos CEPs
  - Validação de formato
  - Remoção de duplicatas

- **Upload de Arquivo**
  - Suporte a Excel (.xlsx, .xls)
  - Suporte a TXT
  - Detecção automática de coluna

### 2. Consulta de CEP
- Processamento em lote
- Tratamento de erros individual
- Feedback em tempo real
- Sistema anti-sobrecarga

### 3. Geocodificação
- Conversão de endereços em coordenadas
- Suporte a múltiplos pontos
- Tratamento de erros de localização

### 4. Visualização
- Mapa interativo
- Múltiplos marcadores
- Popup com informações
- Zoom automático

### 5. Exportação
- Formato CSV
- Formato Excel
- Dados formatados
- Seleção de colunas

## API e Integrações

### ViaCEP
```python
def consultar_cep(cep: str) -> tuple[dict, str]:
    """
    Consulta um CEP na API ViaCEP.
    
    Args:
        cep: string contendo o CEP
        
    Returns:
        tuple: (dados do endereço, mensagem de erro)
    """
```

### Geocodificação
```python
def get_location_coordinates(address: str) -> tuple[float, float]:
    """
    Obtém coordenadas de um endereço usando Nominatim.
    
    Args:
        address: string contendo o endereço completo
        
    Returns:
        tuple: (latitude, longitude)
    """
```

## Processamento de Dados

### Excel
```python
def processar_excel(df: pd.DataFrame) -> list:
    """
    Processa DataFrame do Excel para extrair CEPs.
    
    Args:
        df: DataFrame contendo os dados
        
    Returns:
        list: Lista de CEPs únicos
    """
```

### Validações
- Formato do CEP
- Existência do CEP
- Formato do arquivo
- Dados obrigatórios

## Interface do Usuário

### Componentes
- Tabs de navegação
- Área de upload
- Barra de progresso
- Mapa interativo
- Tabela de resultados
- Botões de download

### Feedback Visual
- Mensagens de sucesso/erro
- Indicador de progresso
- Tooltips informativos
- Validações em tempo real

## Deployment

### Requisitos de Servidor
- Python 3.9+
- 2GB RAM mínimo
- Acesso à internet
- Permissões de escrita

### Configuração
```bash
# Instalação de dependências
pip install -r requirements.txt

# Execução
streamlit run app_v3.py --server.port=8501
```

### Variáveis de Ambiente
```env
DEBUG=False
PORT=8501
CACHE_TTL=3600
```

## Troubleshooting

### Problemas Comuns

1. **Erro na leitura do Excel**
```python
# Verifique o formato do arquivo
# Use modo de compatibilidade
df = pd.read_excel(file, engine='openpyxl')
```

2. **Falha na Geocodificação**
- Verifique conexão com internet
- Implemente retry
- Use cache local

3. **Memória Insuficiente**
- Processe em lotes
- Limpe cache periodicamente
- Otimize dataframes

### Logs e Monitoramento
- Logs de erro detalhados
- Métricas de uso
- Tempo de processamento
- Taxa de sucesso

### Manutenção
- Atualizações regulares
- Backup de dados
- Limpeza de cache
- Monitoramento de API

---

## 📝 Changelog

### [3.0.0] - 2024-02-02
#### Adicionado
- Suporte a Excel
- Multi-consulta
- Mapa interativo
- Download de resultados
- Barra de progresso

#### Modificado
- Interface reformulada
- Processamento otimizado
- Sistema de feedback
- Tratamento de erros

---

>>>>>>> b45c4654b9794f22d302751245e20d2fbccf98fe
Desenvolvido com ❤️ usando Python e Streamlit