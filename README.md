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

## **Zip_xmls.py**
Zip 10.000 XML per time from a folder especified by the user on terminal.
If the number oe XML is not equal divisible by 10.000, the last ZIP saved will have the remaining ones.

## **Requested x sent invoices.py**
Some brazilian companies must deliver a file monthly called EFD ICMS, declaring all operations which ICMS incides over. EFD ICMS is divided by blocks, and there is one, C100, which has a field called invoice key, which is a 44 digit number composed of its operation features. Every invoice is supposed to have a XML, which one this program list as the requested invoices, and the compare it with XML sent.
It's possible to save a list of the requested XML, sent XML and invoice keys that weren't sent yet.

## **unzip all the files inside zip(s)**

## **list csv columns.py**
Listar o cabeçalho de um arquivo csv para facilitar o bulk insert no SQL.
