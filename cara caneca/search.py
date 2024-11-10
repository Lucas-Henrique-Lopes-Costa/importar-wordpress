import os
import pandas as pd
import re

# Caminho para a pasta principal que contém os produtos
base_path = "images"

# Carregar a planilha CSV de produtos
file_path = 'produtos.csv'
produtos_df = pd.read_csv(file_path)

# Corrigir possíveis nomes de colunas com espaços extras ou problemas de codificação
produtos_df.columns = produtos_df.columns.str.strip()

# Lista para armazenar os dados unificados
unified_data = []

# Função para obter título e descrição a partir do arquivo de texto
def extract_title_and_description(txt_file_path):
    title, description = "", ""
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if "título" in line.lower():
                title = lines[i + 1].strip()
            elif "descrição" in line.lower():
                description = lines[i + 1].strip()
    return title, description

# Iterar sobre as linhas do DataFrame
for _, row in produtos_df.iterrows():
    produto = row['Produto']
    link_artes = row['Link Artes']

    # Definir o caminho para a pasta do produto
    categoria_pasta = ""
    if "Caneca" in produto:
        categoria_pasta = "01. Canecas"
    elif "Garrafa Térmica" in produto:
        categoria_pasta = "10. Garrafa Térmica"
    elif "Squeeze" in produto:
        categoria_pasta = "03. Squeeze"
    elif "Cueca" in produto:
        categoria_pasta = "07. Cuecas"
    elif "Copo Térmico" in produto:
        categoria_pasta = "11. Copo Térmico"
    elif "Almofada" in produto:
        categoria_pasta = "02. Almofadas"
    elif "Avental" in produto:
        categoria_pasta = "09. Avental"
    # Adicione mais categorias conforme necessário

    # Caminho completo para a pasta do produto
    pasta_produto_path = os.path.join(base_path, categoria_pasta, link_artes)

    if os.path.exists(pasta_produto_path):
        # Listar os arquivos na pasta e selecionar a primeira imagem
        arquivos = os.listdir(pasta_produto_path)
        imagem = None
        txt_file = None

        for arquivo in arquivos:
            if re.search(r'\.(jpg|jpeg|png)$', arquivo, re.IGNORECASE):
                imagem = arquivo
                break

        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                txt_file = arquivo
                break

        # Extrair título e descrição do arquivo de texto
        if txt_file:
            txt_file_path = os.path.join(pasta_produto_path, txt_file)
            titulo, descricao = extract_title_and_description(txt_file_path)
        else:
            titulo, descricao = "", ""

        # Construir o link do GitHub para a imagem
        github_base_url = "https://github.com/Lucas-Henrique-Lopes-Costa/personalziados/blob/main/cara%20caneca/images"
        imagem_url = f"{github_base_url}/{categoria_pasta}/{link_artes}/{imagem}?raw=true" if imagem else ""

        # Adicionar os dados unificados à lista
        unified_data.append({
            "Produto": produto,
            "Variação 1": row.get('Variação 1', ''),
            "Variação 2": row.get('Variação 2', ''),
            "Preço": row.get('Preço', ''),
            "SKU": row.get('SKU', ''),
            "Estampa": row.get('Estampa', ''),
            "Material": row.get('Material', ''),
            "Tamanho/Medidas": row.get('Tamanho/Medidas', ''),
            "Título": titulo,
            "Descrição": descricao,
            "Link da Imagem": imagem_url
        })

# Criar um DataFrame unificado e salvar como CSV
unified_df = pd.DataFrame(unified_data)
unified_df.to_csv('produtos_unificados.csv', index=False, encoding='utf-8')

print("Planilha unificada criada com sucesso!")