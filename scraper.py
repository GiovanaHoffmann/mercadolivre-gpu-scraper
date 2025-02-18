import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

url = "https://lista.mercadolivre.com.br/placa-de-video#D[A:placa%20de%20video]"

# Headers para evitar bloqueios
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Lista de marcas mais comuns
marcas_conhecidas = {
    "NVIDIA": ["NVIDIA", "Geforce"],
    "AMD": ["AMD"],
    "Intel": ["Intel"],
    "ASUS": ["ASUS"],
    "Gigabyte": ["Gigabyte"],
    "MSI": ["MSI"],
    "EVGA": ["EVGA"],
    "Zotac": ["Zotac"],
    "XFX": ["XFX"],
    "Sapphire": ["Sapphire"],
    "PowerColor": ["PowerColor"]
}

def extrair_marca(titulo):
    titulo_lower = titulo.lower()
    for marca, keywords in marcas_conhecidas.items():
        for keyword in keywords:
            if keyword.lower() in titulo_lower:
                return marca
    return "Desconhecida"

def extrair_capacidade(titulo):
    match = re.search(r"(\d+)\s*(GB|gb|Gb|gB)", titulo)  # regex para captura de "gb"
    return match.group(1) + "GB" if match else "Não informado" # Remove espaço antes de "GB"

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
    hoje = datetime.now().strftime("%Y-%m-%d")
    df.to_csv(f"precos_mercadolivre_{hoje}.csv", index=False, encoding="utf-8")

    print("✅ Dados coletados e salvos em precos_mercadolivre.csv!")
else:
    print("❌ Erro na requisição:", response.status_code)
