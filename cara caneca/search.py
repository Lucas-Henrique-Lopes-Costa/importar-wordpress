import os
import csv

# Caminho da pasta 'images'
folder_path = 'images'

# Nome do arquivo CSV de saída
output_csv = 'file_names.csv'

# Lista para armazenar os nomes dos arquivos
file_names = []

# Percorre todos os arquivos na pasta 'images' e adiciona o caminho completo
for root, dirs, files in os.walk(folder_path):
  for file in files:
    file_names.append(file)

# Ordena os nomes dos arquivos em ordem alfabética
file_names = sorted(file_names)

# Escreve os nomes dos arquivos no arquivo CSV
with open(output_csv, mode='w', newline='') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow(['File Name'])  # Cabeçalho do CSV
  for name in file_names:
    writer.writerow([name])

print(f'Os nomes dos arquivos foram salvos em {output_csv}')