import os
import urllib.parse
import csv
from PIL import Image  # pip install Pillow

# Definir caminho da pasta de imagens
image_folder_path = "images"
output_csv = "franquias.csv"

# Criar ou abrir arquivo CSV para salvar os dados
with open(output_csv, mode="w", newline="") as csvfile:
    fieldnames = ["nome-da-franquia", "foto-da-franquia", "link-google-maps", "tipo"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Percorre todas as subpastas e arquivos dentro de 'images'
    for root, dirs, files in os.walk(image_folder_path):
        # Pega o nome da subpasta, que será o tipo
        if root == image_folder_path:
            # pula a raiz, só quer subpastas
            continue
        tipo = os.path.basename(root)
        for image_file in files:
            if image_file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                image_path = os.path.join(root, image_file)
                try:
                    # Checar se a imagem é quadrada
                    with Image.open(image_path) as img:
                        width, height = img.size
                        if width != height:
                            continue  # pula não-quadradas
                except Exception as e:
                    print(f"Erro ao abrir {image_path}: {e}")
                    continue

                franchise_name = os.path.splitext(image_file)[0]
                encoded_image_file = urllib.parse.quote(image_file)

                # Monta a URL usando a estrutura de pasta correta
                relative_folder = os.path.relpath(root, image_folder_path)
                image_url = f"https://github.com/Lucas-Henrique-Lopes-Costa/personalziados/blob/main/vidadeslots/images/{urllib.parse.quote(relative_folder)}/{encoded_image_file}?raw=true"

                # URL da imagem trocando espaço por '-'
                # encoded_image_file = image_file.replace(" ", "%20")
                # image_url = f"https://vidadeslots.secretogrupo.com/wp-content/uploads/2025/06-07/{encoded_image_file}"

                writer.writerow(
                    {
                        "nome-da-franquia": franchise_name,
                        "foto-da-franquia": image_url,
                        "link-google-maps": "https://bugattif7.com/home?id=147386636&currency=BRL&type=2",
                        "tipo": tipo,
                    }
                )

print(f"Dados salvos em {output_csv}")
