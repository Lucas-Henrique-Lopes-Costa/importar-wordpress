import os
import shutil
import csv

# Caminhos dos diretórios e arquivos
csv_file_path = '/Users/lucashenrique/Projetos/GitHub/personalziados/file_names.csv'
images_dir = '/Users/lucashenrique/Projetos/GitHub/personalziados/images'
select_images_dir = '/Users/lucashenrique/Projetos/GitHub/personalziados/select_images'

# Certifique-se de que o diretório de destino existe
os.makedirs(select_images_dir, exist_ok=True)

# Ler o arquivo CSV e obter a lista de nomes de arquivos
with open(csv_file_path, newline='') as csvfile:
  reader = csv.reader(csvfile)
  file_names = [row[0] for row in reader]

# Função para varrer diretório recursivamente e encontrar arquivos correspondentes
def find_file_in_directory(file_name, directory):
  for root, _, files in os.walk(directory):
    if file_name in files:
      return os.path.join(root, file_name)
  return None

# Copiar os arquivos selecionados para o diretório de destino
for file_name in file_names:
  source_path = find_file_in_directory(file_name, images_dir)
  if source_path:
    destination_path = os.path.join(select_images_dir, file_name)
    shutil.copy(source_path, destination_path)
    print(f'Arquivo {file_name} copiado para {select_images_dir}')
  else:
    print(f'Arquivo {file_name} não encontrado em {images_dir}')