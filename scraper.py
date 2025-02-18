import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://lista.mercadolivre.com.br/placa-de-video#D[A:placa%20de%20video]"

# Headers para evitar bloqueios
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Lista de marcas mais comuns
marcas_conhecidas = ["NVIDIA", "AMD", "Intel", "ASUS", "Gigabyte", "MSI", "EVGA", "Zotac", "XFX", "Sapphire", "PowerColor", "Geforce"]

def extrair_marca(titulo):
    for marca in marcas_conhecidas:
        if marca.lower() in titulo.lower():
            return marca
    return "Desconhecida"

def extrair_capacidade(titulo):
    match = re.search(r"(\d+)\s?(GB|gb|Gb)", titulo)  # regex para captura de "gb"
    return match.group(0).upper() if match else "Não informado"

# Requisição para o site
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    produtos = []
    
    # Busca os blocos de produtos no html
    for item in soup.find_all("div", class_="poly-card__content"):
        titulo = item.find("a", class_="poly-component__title")
        preco_inteiro = item.find("span", class_="andes-money-amount__fraction")
        preco_centavos = item.find("span", class_="andes-money-amount__cents andes-money-amount__cents--superscript-24")
        
        if titulo and preco_inteiro:
            nome = titulo.text.strip()
            
            # Remove separadores de milhar do preço inteiro
            preco = preco_inteiro.text.replace('.', '').strip()
            
            # Adiciona os centavos, se existirem
            if preco_centavos:
                preco += f".{preco_centavos.text.strip()}"
            else:
                preco += ".00"
            
            preco = float(preco.replace(',', '.'))
            marca = extrair_marca(nome)
            capacidade = extrair_capacidade(nome)
            
            produtos.append([nome, preco, marca, capacidade])

    df = pd.DataFrame(produtos, columns=["Produto", "Preço", "Marca", "Capacidade"])
    df.to_csv("precos_mercadolivre.csv", index=False, encoding="utf-8")

    print("✅ Dados coletados e salvos em precos_mercadolivre.csv!")
else:
    print("❌ Erro na requisição:", response.status_code)
