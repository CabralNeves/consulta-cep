# Documentação - Consulta CEP App

## 📋 Sumário
1. [Visão Geral](#visão-geral)
2. [Arquitetura](#arquitetura)
3. [Instalação](#instalação)
4. [Configuração](#configuração)
5. [Uso](#uso)
6. [API](#api)
7. [Estrutura do Projeto](#estrutura-do-projeto)
8. [Deployment](#deployment)
9. [Contribuição](#contribuição)
10. [Troubleshooting](#troubleshooting)

## Visão Geral

O Consulta CEP App é uma aplicação web desenvolvida em Python utilizando o framework Streamlit para fornecer uma interface intuitiva de consulta de endereços através do CEP. A aplicação consome a API ViaCEP e apresenta os resultados de forma organizada e amigável.

### Principais Funcionalidades
- Consulta de CEP em tempo real
- Interface responsiva e moderna
- Validação automática de entrada
- Cópia rápida de endereço completo
- Tratamento de erros amigável

## Arquitetura

```
Consulta CEP App
├── Frontend (Streamlit)
│   └── Interface do Usuário
├── Backend (Python)
│   ├── Processamento de CEP
│   └── Validações
└── API Externa
    └── ViaCEP
```

### Tecnologias Utilizadas
- Python 3.9+
- Streamlit 1.31.1
- Requests 2.31.0
- Pandas 2.2.0
- Python-dotenv 1.0.1

## Instalação

### Requisitos
- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo a Passo

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/consulta-cep.git
cd consulta-cep
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração

### Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
DEBUG=False
PORT=8501
```

### Configuração do VS Code
```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.linting.enabled": true
}
```

## Uso

### Executando Localmente
```bash
streamlit run app.py
```

### Utilizando a Aplicação
1. Acesse a aplicação no navegador (padrão: http://localhost:8501)
2. Digite o CEP desejado no campo de busca
3. Clique no botão "Buscar" ou pressione Enter
4. Visualize os resultados
5. Use o botão "Copiar endereço completo" se necessário

## API

### Função Principal
```python
def consultar_cep(cep: str) -> tuple[dict, str]:
    """
    Consulta um CEP na API ViaCEP.
    
    Args:
        cep (str): CEP a ser consultado
        
    Returns:
        tuple: (dados do endereço, mensagem de erro)
    """
```

### Respostas da API
```python
# Sucesso
{
    'cep': '12345-678',
    'logradouro': 'Rua Exemplo',
    'bairro': 'Centro',
    'cidade': 'São Paulo',
    'uf': 'SP'
}

# Erro
None, "Mensagem de erro"
```

## Estrutura do Projeto
```
consulta-cep/
├── app.py              # Arquivo principal
├── requirements.txt    # Dependências
├── .env               # Variáveis de ambiente
├── .gitignore         # Arquivos ignorados
├── README.md          # Documentação básica
├── Procfile           # Configuração de deploy
└── runtime.txt        # Versão do Python
```

## Deployment

### EasyPanel
1. Configure o servidor:
```bash
# Atualize o sistema
apt update && apt upgrade -y

# Instale dependências
apt install python3-pip python3-venv -y
```

2. Configure o aplicativo no EasyPanel:
- Nome: consulta-cep
- Comando: `streamlit run app.py`
- Porta: 8501

### Nginx (se necessário)
```nginx
server {
    listen 80;
    server_name seu-dominio.com;
    
    location / {
        proxy_pass http://localhost:8501;
    }
}
```

## Contribuição

### Como Contribuir
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Padrões de Código
- PEP 8 para Python
- Docstrings em todas as funções
- Testes para novas funcionalidades
- Commits semânticos

## Troubleshooting

### Problemas Comuns

1. **Erro de Instalação**
```bash
# Solução
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

2. **Erro de Conexão**
- Verifique sua conexão com a internet
- Confirme se a API ViaCEP está online

3. **Problemas no Deploy**
- Verifique as portas no firewall
- Confirme as configurações do Nginx
- Verifique os logs do aplicativo

### Suporte
Para suporte, abra uma issue no GitHub ou entre em contato via [seu-email@exemplo.com].

---

## 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido com ❤️ usando Python e Streamlit