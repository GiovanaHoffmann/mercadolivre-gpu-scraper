# GPU Price Pipeline

## Descrição do Projeto
Este projeto consiste em um pipeline de dados que realiza web scraping de preços de placas de vídeo no Mercado Livre, processa os dados extraídos e os armazena em um banco de dados PostgreSQL. O objetivo é criar um fluxo automatizado de coleta, transformação e armazenamento de informações sobre os preços de GPUs, facilitando futuras análises.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto
- **BeautifulSoup**: Biblioteca para extração de dados do HTML
- **Requests**: Para realizar requisições HTTP
- **Pandas**: Para manipulação e tratamento de dados
- **PostgreSQL**: Banco de dados relacional para armazenar os dados coletados
- **psycopg2**: Biblioteca para conectar o Python ao PostgreSQL
- **dotenv**: Para gerenciamento de credenciais sensíveis

## Estrutura do Projeto
```
web_scraper_project/
│── scraper.py         # Script de web scraping
│── pipeline.py        # Script para inserção dos dados no PostgreSQL
│── .env               # Arquivo para armazenar credenciais do banco
│── precos_mercadolivre.csv  # Arquivo CSV gerado pelo scraper
│── requirements.txt   # Dependências do projeto
│── README.md          # Documentação do projeto
```

## Como Executar o Projeto
### 1. Clonar o repositório
```bash
git clone https://github.com/seuusuario/gpu-price-pipeline.git
cd gpu-price-pipeline
```

### 2. Criar e ativar um ambiente virtual
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as credenciais do banco
Crie um arquivo `.env` na raiz do projeto e defina as credenciais do PostgreSQL:
```
DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

### 5. Executar o Web Scraper
```bash
python scraper.py
```
Isso gerará um arquivo `precos_mercadolivre.csv` com os dados extraídos.

### 6. Executar o Pipeline de Dados
```bash
python pipeline.py
```
Os dados serão inseridos no banco de dados PostgreSQL.

## Exemplo de Saída (CSV e Banco de Dados)
| Produto | Preço | Marca | Capacidade |
|---------|--------|--------|------------|
| RTX 3060 | 2.499,00 | NVIDIA | 12GB |
| RX 6700 XT | 3.299,00 | AMD | 12GB |

---
**Desenvolvido por Giovana Araújo Hoffmann** 

