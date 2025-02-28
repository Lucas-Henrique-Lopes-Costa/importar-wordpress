import requests
import zipfile
import os

# Lista de URLs das imagens
image_urls = [
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0029_Dynapac-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0030_Forza-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0031_Foton-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0032_Furlan-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0034_HANGCHA-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0035_Hitachi-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0036_Hyundai-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0037_Komatsu-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0038_John_Deere_linha_Amarela-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0039_Liebherr-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0040_Link-BELT_EXACAVATORS-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0041_LiuGong-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0042_Lonking-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0043_Manitou-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0044_Metso-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0045_Michigan-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0046_New_Holland_linha_Amarela-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0047_Yanmar-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0048_YALE-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0001s_0049_XCMG-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0002s_0000_FORD-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0002s_0001_IVECO-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0002s_0002_MAN-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0002s_0003_MERCEDES-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0002s_0004_SCANIA-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0002s_0005_VOLKSWAGEN-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0002s_0006_DAF-removebg-preview.png.webp",
    "https://centraldeusadas.agenciakaizen.com.br/wp-content/uploads/2025/01/logos-300x300px_0002s_0007_Volvo.png.webp"
]

# Pasta temporária para armazenar imagens
temp_dir = "/Users/lucashenrique/Projetos/Github/importar-wordpress/central de usados/imagens"
os.makedirs(temp_dir, exist_ok=True)

# Baixar as imagens
image_files = []
for i, url in enumerate(image_urls):
    file_path = os.path.join(temp_dir, f"image_{i}.webp")
    response = requests.get(url)
    with open(file_path, "wb") as file:
        file.write(response.content)
    image_files.append(file_path)

# Criar um arquivo ZIP com as imagens
zip_path = "/mnt/data/logos_carrossel.zip"
with zipfile.ZipFile(zip_path, "w") as zipf:
    for image in image_files:
        zipf.write(image, os.path.basename(image))

# Retornar o caminho do arquivo ZIP
zip_path
