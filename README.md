# Automatizations
Here are some useful programas for my current job. Reminding that I've coded these programs to be accesible to laypeople use these programs.

## PDF merger.py:
3 types of merge, which ones the user especifies answering the program questions:
- merge all PDFs from a folder
- merge only 1 page from all PDFs of a folder
- merge multiple pages from all PDFs of a folder

The final file is saved in the same folder of the PDFs.

## **Copy a list of files from a folder to another one.py**
The user interacts in the terminal to especify some features, as the folder where are the files and the folder to save the files.

## **Zip_xmls**
Zip 10.000 XML per time from a folder especified by the user on terminal.
If the number oe XML is not equal divisible by 10.000, the last ZIP saved will have the remaining ones.

## **NFs solicitadas x enviadas.py**
Esse programa verifica se os XML das NF solicitados foram enviados. Para isso, é possível passar arquivo csv com as chaves das NF solicitadas ou passar o caminho da pasta pra extrair essas chaves do C100 do SPED. Ainda, é possível também passar um arquivo csv com os nomes dos XML ENVIADOS ou passar o caminho da pasta onde o programa vai extrair o nome dos arquivos XML. Após ter a lista de chaves das NF solicitadas, o programa confronta com a lista com os XML enviados, possibilitando o usuário baixar a lista de chaves de NF solicitadas, XML enviados, as chaves cujos XML foram enviados e as chaves cujos XML NÃO foram enviados (i.e continuam pendentes)

## **deszipar os zips de uma pasta até que não restem mais zips (zips dentro de zips)**
Esse programa verifica se os valores de uma coluna de um CSV estão em outro CSV. 

## **listar colunas csv.py**
Listar o cabeçalho de um arquivo csv para facilitar o bulk insert no SQL.
