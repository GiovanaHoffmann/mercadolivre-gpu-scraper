import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

df = pd.read_csv("precos_mercadolivre.csv")

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)
cursor = conn.cursor()

cursor.execute('''               
CREATE TABLE IF NOT EXISTS precos_placas_video (
    id SERIAL PRIMARY KEY,
    produto TEXT,
    preco NUMERIC,
    marca TEXT,
    capacidade TEXT,
    data_coleta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')

# Inserindo os dados no banco
for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO precos_placas_video (produto, preco, marca, capacidade) VALUES (%s, %s, %s, %s)", 
        (row["Produto"], row["Preço"], row["Marca"], row["Capacidade"])
    )

conn.commit()
cursor.close()
conn.close()

print("✅ Dados inseridos no PostgreSQL com sucesso!")
