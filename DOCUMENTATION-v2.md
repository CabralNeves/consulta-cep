# Documentação - Consulta CEP App v2.0

## 📋 Sumário
1. [Visão Geral](#visão-geral)
2. [Novidades](#novidades)
3. [Instalação](#instalação)
4. [Configuração](#configuração)
5. [Uso](#uso)
6. [API e Integrações](#api-e-integrações)
7. [Estrutura do Projeto](#estrutura-do-projeto)
8. [Deployment](#deployment)
9. [Troubleshooting](#troubleshooting)

## Visão Geral
A versão 2.0 do Consulta CEP App adiciona funcionalidades de geolocalização e visualização em mapa, mantendo todas as funcionalidades da v1.0.

### Melhorias da v2.0
- Integração com OpenStreetMap
- Visualização de mapa interativo
- Interface em tela cheia
- Melhor organização visual
- Geocodificação de endereços

## Arquitetura

```
Consulta CEP App v2.0
├── Frontend (Streamlit)
│   ├── Interface do Usuário
│   └── Mapa Interativo (Folium)
├── Backend (Python)
│   ├── Processamento de CEP
│   ├── Geocodificação
│   └── Validações
└── APIs Externas
    ├── ViaCEP
    └── OpenStreetMap
```

## Instalação

### Requisitos Adicionais v2.0
- folium==0.15.1
- geopy==2.4.1
- streamlit-folium==0.18.0

### Instalação Completa
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/consulta-cep.git

# Entre no diretório
cd consulta-cep

# Instale as dependências
pip install -r requirements.txt
```

## Uso do Mapa

### Funcionalidades do Mapa
- Zoom in/out
- Arrastar para navegar
- Círculo de 500m de raio
- Marcador de localização exata

### Limitações
- Depende da precisão do OpenStreetMap
- Requer conexão com internet
- Pode ter variações na precisão da localização

## API e Integrações

### ViaCEP
```python
def consultar_cep(cep: str) -> tuple[dict, str]:
    """Consulta um CEP na API ViaCEP."""
```

### Geocodificação
```python
def get_location_coordinates(address: str) -> tuple[float, float]:
    """Obtém coordenadas de um endereço."""
```

## Estrutura do Projeto v2.0
```
consulta-cep/
├── app_v1.py           # Versão 1.0
├── app_v2.py           # Versão 2.0
├── requirements.txt    # Dependências
├── .env               # Variáveis de ambiente
├── .gitignore         # Arquivos ignorados
├── README.md          # Documentação básica
├── README-v2.md       # Documentação v2.0
└── DOCUMENTATION-v2.md # Documentação técnica v2.0
```

## Deployment

### Considerações Adicionais v2.0
- Maior consumo de memória
- Necessidade de HTTPS para geolocalização
- Cache de mapas recomendado

### Configuração do Servidor
```bash
# Instale as dependências adicionais
sudo apt-get install python3-dev
pip install -r requirements.txt
```

## Troubleshooting

### Problemas Comuns v2.0

1. **Mapa não carrega**
```python
# Verifique a conexão com OpenStreetMap
# Verifique se as coordenadas são válidas
```

2. **Lentidão no carregamento**
- Implemente cache de mapas
- Otimize as consultas de geocodificação

3. **Erros de Geocodificação**
- Verifique o formato do endereço
- Implemente retry em caso de falha

### Próximos Passos
- Implementação de cache
- Otimização de performance
- Suporte a múltiplos provedores de mapas

---

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido com ❤️ usando Python e Streamlit