# Caso vc queira entender o código, fiz um explicativo no final
# Aperte F5 e preste atenção no terminal (dê um enter pro Python processar a informação que vc inseriu)

import xml.etree.ElementTree as ET
import os
import csv

print("Esse programa extrai o número da chave da NFe de vários XMLs que estiverem na mesma pasta.")
pasta = input("\nCopie o caminho da pasta onde estejam os XMLs e clique com o botão direito do mouse aqui para colar >>>> ").replace('\\','/')

lista_xmls = []

for filename in os.listdir(pasta):                                      # pra cada elemento (arquivo, pasta, etc) dentro da pasta
    if filename.endswith('.xml'):                                       # se o elemento terminar com .xml:
        xml_file_path = os.path.join(pasta, filename)                   # variável com o caminho da pasta + nome do arquivo
        tree = ET.parse(xml_file_path)                                  # analisa o arquivo xml
        root = tree.getroot()                                           # retorna os elementos raiz do XML
        for item in root.iter():                                        # pra cada item dentro das raízes:
            if item.tag == '{http://www.portalfiscal.inf.br/nfe}chNFe': # se a tag for essa
                lista_xmls.append(item.text)                            # adiciona o elemento dessa tag na lista_xmls
print(lista_xmls)

pasta_csv = pasta + '/lista_xmls.csv'
with open(pasta_csv, 'w', newline='') as f:                             # newline = '' pra evitar do python criar o CSV pulando uma linha entre os valores
    write = csv.writer(f, delimiter = ',')
    for element in lista_xmls:
        write.writerow(element)



# consegui grande parte desse código aqui: https://raccoon.ninja/pt/dev-pt/manipulando-xml-com-python/ e tbm do chatgpt, pesquisando por:

''' 
Sobre XMLs e ElementTree:

XML é uma extensão de arquivo usado apenas para exibir informações com uma certa estrutura.
-> ELEMENTOS FILHOS (element child): seções do XML
-> ELEMENTO RAIZ (element root): é o elemento que fica no topo da sequência, ele é o 'pai' dos elementos 'filhos' (ele começa no começo da linha, os elementos ficam identados a ele)
-> TAGS: são identificadores dos elementos. P/ delimitar um elemento, deve ter uma tag de início e outra de final, ficando assim: <*tag_inicio*> element child <*tag_final*>
Ex: 
<*nome_usuario*>        -> elemento raiz
    <nome>Fulano</nome> -> elemento filho
    <idade>25</idade>   -> elemento filho
    etc                 -> elementos filhos
</*nome_usuario*>       -> final desse elemento raiz

O processo de ler um XML e analisar seus componentes é chamada de PARSING.
ElementTree é uma biblioteca que fornece ferramentas para manipular XMLs. Ela já vem junto com o Python, portanto não precisa instalá-la

Ler um XML com ElementTree:
tree = ET.parse('movies.xml')       -> cria uma variável tree que lê/analisa o arquivo movies.xml
root = tree.getroot()               -> getroot retorna os elementos raízes

Vc consegue iterar sobre os subelementos de root fazendo:
for item in root.ier():
Se quiser acessar algum ELEMENTO FILHO, use item.text
Se quiser acessar alguma tag, use item.tag

'''





