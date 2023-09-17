# Criar zips com 10.000 xmls por zip. Aperte F5 pra rodar e preste atenção no terminal
# Vc deve deixar todos os XMLs que vc deseja zipar numa mesma pasta. Não deixe em subpastas!!!

import zipfile
import pathlib
import os

caminho_pasta_xmls = input("\nCopie o caminho da pasta de origem dos arquivos e clique com o botão direito do mouse aqui para colar. Os zips serão colados nessa mesma pasta >>>> ").replace('\\','/')
directory = pathlib.Path(caminho_pasta_xmls)

#count how many XMLs are in the directory:
xml_files = [file for file in directory.iterdir() if file.is_file() and file.suffix.lower() == '.xml'] #mantém apenas o que for file + final '.xml'
counter_xml = len(xml_files)
print(f"There are {counter_xml} xmls in the directory")

                                                                    
i = 0                                                                #zip file counter
zip_size = 10000

while i * zip_size <= counter_xml:
    zip_name = str(caminho_pasta_xmls)+'/grupo_xml_'+str(i)+'.zip'   # define o diretório e o nome do zip
    grupo_xml_i = zipfile.ZipFile(zip_name, 'w')                     # cria o zip
    
    for j in range(i * zip_size, min((i + 1) * zip_size, counter_xml)): #pra cada número dentro do intervalo (mínimo = i * 10k, máximo = mínimo entre (10k * i + 1 e a qtde de xmls na pasta))
        file_path = xml_files[j]                                    # atribui o xml à file_path
        grupo_xml_i.write(file_path, arcname = file_path.name)      # coloca o xml no zip
    grupo_xml_i.close()
    i+=1                                                            # repete tudo pro zip + 1

print('''O nome dos .zips serão "grupo_xml_i", onde i = 1,2,3 etc''')
                
            
