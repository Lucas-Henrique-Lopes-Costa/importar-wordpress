import os
import csv
from urllib.parse import quote
import unicodedata

# URL base para gerar o link da imagem (não altere o final, pois será acrescentado o nome da pasta e da imagem)
BASE_URL = "https://github.com/Lucas-Henrique-Lopes-Costa/importar-wordpress/blob/main/cvm"

# Pasta raiz onde estão os cursos (pastas)
ROOT_FOLDER = "cvm"

# Obtém a lista de pastas (cursos) dentro da pasta ROOT_FOLDER
course_folders = [folder for folder in os.listdir(ROOT_FOLDER) if os.path.isdir(os.path.join(ROOT_FOLDER, folder))]

# Cria o CSV no mesmo diretório do main.py
with open("cursos.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # Escreve o cabeçalho do CSV com a nova coluna "Area"
    writer.writerow(["Curso", "Link", "Area"])
    
    # Percorre cada pasta de curso
    for course in course_folders:
        course_path = os.path.join(ROOT_FOLDER, course)
        # Lista arquivos que sejam imagens (adicione outras extensões se necessário)
        image_files = [f for f in os.listdir(course_path) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))]
        
        if not image_files:
            print(f"Nenhuma imagem encontrada na pasta '{course}'.")
            continue
        
        # Ordena e seleciona o primeiro arquivo de imagem
        image_files.sort()
        image_file = image_files[0]
        
        # Força a normalização para NFC usando encode-decode para garantir a composição
        course_normalized = unicodedata.normalize('NFC', course).encode('utf-8').decode('utf-8')
        image_normalized = unicodedata.normalize('NFC', image_file).encode('utf-8').decode('utf-8')
        
        # Codifica os nomes para garantir que a URL fique correta (trata espaços e caracteres especiais)
        course_encoded = quote(course_normalized)
        image_encoded = quote(image_normalized)
        
        # Monta a URL no formato desejado
        image_url = f"{BASE_URL}/{course_encoded}/{image_encoded}?raw=true"
        
        # Formata o nome do curso: remove underscores, converte para minúsculas e capitaliza apenas a primeira letra
        formatted_course = course.replace("_", " ").lower().capitalize()
        
        # Escreve a linha no CSV com o nome formatado, a URL e a área "Profissionalizante"
        writer.writerow([formatted_course, image_url, "Profissionalizante"])
        print(f"Processado: Curso: {formatted_course} | Link: {image_url} | Area: Profissionalizante")

print("Arquivo CSV 'cursos.csv' gerado com sucesso!")
