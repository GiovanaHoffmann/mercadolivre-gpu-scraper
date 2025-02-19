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
- **unittest**: Para testes unitários

## Estrutura do Projeto
```
web_scraper_project/
|── dados/                # Pasta para armazenar os arquivos CSV gerados
|    ├── precos_mercadolivre_YYYY-MM-DD.csv  # Arquivo CSV gerado pelo scraper (data dinâmica)
|── scraper.py            # Script de web scraping
|── pipeline.py           # Script para inserção dos dados no PostgreSQL
|── executar_pipeline.py  # Script para executar scraper.py e pipeline.py automaticamente
|── test_scraper.py       # Testes unitários para funções de extração de dados
|── test_pipeline.py      # Testes unitários para a inserção no banco
|── .env                  # Arquivo para armazenar credenciais do banco
|── requirements.txt      # Dependências do projeto
|── README.md             # Documentação do projeto
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

### 5. Executar Web Scraper e Pipeline Automaticamente
Para realizar o scraping e inserir os dados no banco em sequência:
```bash
python executar_pipeline.py
```
Isso gerará um arquivo CSV dentro da pasta `dados/` e em seguida os dados serão inseridos no PostgreSQL.

## Testes Unitários
O projeto inclui testes unitários para garantir que as funções críticas funcionem corretamente.

### 6. Executar os Testes
```bash
python -m unittest discover
```
Ou execute os testes individualmente:
```bash
python test_scraper.py
python test_pipeline.py
```

## Armazenamento Incremental
Para evitar sobrescrita de dados, o pipeline de inserção no banco de dados verifica se um produto já está presente antes de inseri-lo. Isso garante que os preços históricos sejam mantidos ao longo do tempo.

## Exemplo de Saída (CSV e Banco de Dados)
| Produto    | Preço   | Marca | Capacidade |
|------------|--------|--------|------------|
| RTX 3060  | 2.499,00 | NVIDIA | 12GB |
| RX 6700 XT | 3.299,00 | AMD | 12GB |

---
**Desenvolvido por Giovana Araújo Hoffmann**

