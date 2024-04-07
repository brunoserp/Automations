# automatizacoes
Alguns processos mecânicos que automatizei

## pdf merger.py:**

Junta vários PDFs em um só por meio de interações com o usuário.

Há 3 tipos de processos:
- juntar todos os PDFs
- juntar apenas 1 página de todos os PDFs
- juntar uma sequência de páginas de todos os PDFs

O arquivo final é criado na mesma pasta que tiverem todos os PDFs.

## **copiar todos os arquivos dentro de uma pasta para uma outra pasta.py**
Esse programa serve pra facilitar o trabalho de entrar em todas as pastas presentes dentro de uma pasta e colar numa outra pasta.
Há uma interação com o usuário para ele informar a pasta de origem dos arquivos e a pasta onde o python vai colar os arquivos (a pasta de destino deve estar fora da pasta de origem)

## **zipar_xmls**

Esse programa serve pra zipar 10.000 XMLs de determinada pasta indicada pelo usuário por vez.
Assim, se tiver 16.520 XMLs na pasta ele vai fazer um zip com 10.000 XMLs e outro com 6.520.

## **NFs solicitadas x enviadas.py**
Esse programa verifica se os XML das NF solicitados foram enviados. Para isso, é possível passar arquivo csv com as chaves das NF solicitadas ou passar o caminho da pasta pra extrair essas chaves do C100 do SPED. Ainda, é possível também passar um arquivo csv com os nomes dos XML ENVIADOS ou passar o caminho da pasta onde o programa vai extrair o nome dos arquivos XML. Após ter a lista de chaves das NF solicitadas, o programa confronta com a lista com os XML enviados, possibilitando o usuário baixar a lista de chaves de NF solicitadas, XML enviados, as chaves cujos XML foram enviados e as chaves cujos XML NÃO foram enviados (i.e continuam pendentes)


## **deszipar os zips de uma pasta até que não restem mais zips (zips dentro de zips)**



Esse programa verifica se os valores de uma coluna de um CSV estão em outro CSV. 

