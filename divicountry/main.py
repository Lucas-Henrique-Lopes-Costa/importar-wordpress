import os
import csv
import urllib.parse

# Define o caminho absoluto para o diretório onde main.py está localizado
pasta_atual = os.path.dirname(os.path.abspath(__file__))
# Junta o diretório atual com a pasta 'imagens'
pasta_imagens = os.path.join(pasta_atual, "imagens")

# Verifica se a pasta existe
if not os.path.exists(pasta_imagens):
    raise FileNotFoundError(f"A pasta '{pasta_imagens}' não foi encontrada.")

# URL base conforme seu exemplo
base_url = "https://raw.githubusercontent.com/Lucas-Henrique-Lopes-Costa/importar-wordpress/refs/heads/main/divicountry/imagens/"

# Lista todos os arquivos na pasta de imagens
arquivos = os.listdir(pasta_imagens)

# Nome do arquivo CSV que será gerado
nome_csv = "imagens.csv"

with open(nome_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Escreve o cabeçalho do CSV
    writer.writerow(["nome", "link"])
    
    # Processa cada arquivo encontrado
    for arquivo in arquivos:
        # Extrai o nome sem a extensão
        nome_sem_extensao, _ = os.path.splitext(arquivo)
        # Cria o link codificando o nome do arquivo para URL
        link = base_url + urllib.parse.quote(arquivo)
        # Escreve uma linha no CSV com o nome sem extensão e o link
        writer.writerow([nome_sem_extensao, link])

print(f"Arquivo CSV '{nome_csv}' criado com sucesso!")
