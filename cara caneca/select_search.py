import csv

import urllib.parse

# Função para gerar o URL
def generate_url(file_path):
  base_url = "https://github.com/Lucas-Henrique-Lopes-Costa/personalziados/blob/main/cara%20caneca/"
  encoded_path = urllib.parse.quote(file_path)
  return f"{base_url}{encoded_path}?raw=true"

# Lendo os arquivos CSV
with open('/Users/lucashenrique/Projetos/GitHub/personalziados/cara caneca/file_names.csv', newline='') as file_names_csv:
  file_names_reader = csv.reader(file_names_csv)
  file_names = list(file_names_reader)

with open('/Users/lucashenrique/Projetos/GitHub/personalziados/cara caneca/produtos.csv', newline='') as produtos_csv:
  produtos_reader = csv.DictReader(produtos_csv)
  produtos = list(produtos_reader)

# Relacionando e gerando URLs
urls = []
for produto in produtos:
  pasta = produto['Nome Pasta']
  for file_name in file_names:
    file_path = f"{pasta}/{file_name[0]}"
    url = generate_url(file_path)
    urls.append(url)

# Exibindo os URLs gerados
for url in urls:
  print(url)
  # Escrevendo os URLs gerados em um novo arquivo CSV
  with open('/Users/lucashenrique/Projetos/GitHub/personalziados/cara caneca/produtos_import.csv', mode='w', newline='') as produtos_import_csv:
    fieldnames = ['Nome Pasta', 'URL']
    writer = csv.DictWriter(produtos_import_csv, fieldnames=fieldnames)

    writer.writeheader()
    for produto, url in zip(produtos, urls):
      writer.writerow({'Nome Pasta': produto['Nome Pasta'], 'URL': url})