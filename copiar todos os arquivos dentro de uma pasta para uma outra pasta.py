# Dê um F5 e preste atenção no terminal

import shutil
import os
import pathlib
print("Esse programa vai extrair todos os arquivos de dentro de uma pasta (incluindo arquivos dentro de subpastas) para outra pasta. A pasta de origem dos arquivos e a pasta que ele vai colar os arquivos não podem ser iguais.\nEsse programa serve pra facilitar o trabalho de entrar em todas as pastas presentes dentro de uma pasta e colar numa outra pasta.")

# Insira, em src, o caminho da pasta que estão os arquivos que vc queira copiar
src = input("\nCopie o caminho da pasta de origem (que o Python vai extrair os arquivos de dentro) e clique com o botão direito do mouse aqui para colar >>>> ").replace('\\','/')
# Insira, em dest, o caminho da pasta que vc queira colar os arquivos
dest = input("\nCopie o caminho da pasta de destino (que o Python vai salvar os arquivos) e clique com o botão direito do mouse aqui para colar >>>> ").replace('\\','/')

# Há alguma extensão desejada?
extensao = input("Há alguma extensão desejada? Se sim, informe, e o Python só vai extrair essa extensão. Caso não tiver, aperte enter >>> ")
# Se a extensao nao começar com ponto final, adicionar:
if extensao != '':
    if not extensao.startswith('.'):
        extensao = '.' + extensao

os.makedirs(dest, exist_ok=True)

for dirpath, _, filenames in os.walk(src):          # os.walk: trilha um caminho dentro da pasta de src (acessa todas as pastas dentro da pasta indicada)
    for file in filenames:                          # pra cada arquivo dentro do src
        if extensao == '':
            src_file = os.path.join(dirpath, file)      # os.path.join() junta arquivos (diretório dos arquivos, arquivos a serem juntados)
            dest_file = os.path.join(dest, file)
            shutil.copyfile(src_file, dest_file)        # copia o arquivo do 1º argumento e cola no 2º argumento
        
        else:
            if file.endswith(extensao):
                src_file = os.path.join(dirpath, file)
                dest_file = os.path.join(dest, file)
                shutil.copyfile(src_file, dest_file)
