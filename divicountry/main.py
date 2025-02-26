# faça um código que leia a pasta imagens e retorne o nome de todas as imagens que estão dentro da pasta

import os

def main():
    # Listando o conteúdo da pasta
    path = '/Users/lucashenrique/Projetos/Github/importar-wordpress/divicountry/imagens'
    files = os.listdir(path)

    # Listando apenas os arquivos
    files = [file for file in files if os.path.isfile(os.path.join(path, file))]
    # da uma quebra de linha para cada nome da imagem e rmeove a extensão do arquivo
    files = [file.split('.')[0] for file in files]
    # Imprime o nome de cada imagem
    for file in files:
        print(file)
        


if __name__ == '__main__':
    main()
