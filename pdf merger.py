# Programa pra juntar PDFs num PDF só. Os PDFs a serem juntados devem estar todos na mesma pasta
# P/ rodar o programa, aperte F5 e responda o que aparecer no terminal. Aperte enter pra enviar sua resposta

import os
import PyPDF2
merger = PyPDF2.PdfMerger()

''' Abaixo são 3 tipos de merge que o usuário pode fazer:
1) todo_pdf: juntar todas as páginas dos pdfs desejados
2) unica_pag: juntar apenas 1 página de todos os pdfs desejados
3) sequencia_pag: juntar uma sequência de páginas de todos os pdfs desejados'''

# 1):
def todo_pdf(pasta, nome_arquivo="/pdf_merged.pdf"):
    merger = PyPDF2.PdfMerger()
    for file in os.listdir(pasta):
        if file.endswith('.pdf'):
            merger.append(f"{pasta}/{file}")

    merger.write(pasta+'/'+nome_arquivo)
    merger.close()

# 2):
def unica_pag(pasta, pages, nome_arquivo):
    merger = PyPDF2.PdfMerger()
    for file in os.listdir(pasta):
        if file.endswith('.pdf'):
            merger.append(f"{pasta}/{file}", pages=pages)
    print(pasta+'/'+nome_arquivo)
    merger.write(f'{pasta}/{nome_arquivo}')
    merger.close()

# 3):
def sequencia_pag(pasta, pages, nome_arquivo = "/pdf_merged.pdf"):
    for file in os.listdir(pasta):
        if file.endswith('.pdf'):
            x = PyPDF2.PdfReader(pasta+'/'+file)
            qtd_pag = len(x.pages)
            if qtd_pag < len(x.pages):
                print(f"O arquivo {file} tem menos páginas do que a(s) que vc quer. Por ex vc quer a 8ª página de um pdf que tem 4 páginas")
            merger.append(f"{pasta}/{file}", pages)

    merger.write(pasta + '/' + nome_arquivo)
    merger.close()

#____________________________________________________________________________________________________________________________________________________
'''Abaixo são as funções que serão executadas conforme o usuário vai respondendo os inputs:'''

# pergunta ao usuário a pasta que estão os pdfs que vão ser juntados. Essa pasta será tbm onde o python vai criar o pdf final
def user_pasta():
    pasta = input("\nCopie o caminho dessa pasta e clique com o botão direito do mouse aqui >>>> ").replace('\\','/')
    print(f'oiii, {pasta}')
    pasta_confirmacao = input(f"\nO caminho da pasta que vc inseriu é\n{pasta}.\nS para confirmar e n para negar: ").lower()
    # Enquanto o usuário não digitar s, continuar perguntando a pasta e a confirmação
    while pasta_confirmacao != 's':
        pasta = input("\nCopie o caminho dessa pasta e clique com o botão direito do mouse aqui >>>> ").replace('\\','/')
        pasta_confirmacao = input(f"\nO caminho da pasta que vc inseriu é\n{pasta}\nS para confirmar e n para negar: ").lower()
    return pasta

# pergunta ao usuário o nome do arquivo (pdf) final
def user_nome_arqv():
    nome_arquivo = input("\nInsira o nome do arquivo PDF que vc quer que o python salve\nCaso não tenha preferência, aperte enter, o Python vai salvar como pdf_merged.pdf. O arquivo será salvo na mesma pasta que vc indicou na pergunta anterior. ")
    if nome_arquivo == '':
        nome_arquivo = "pdf_merged.pdf"
    elif not nome_arquivo.endswith('.pdf'):
            nome_arquivo = nome_arquivo + '.pdf'
            #depois que o nome_arquivo foi ajustado, vamos à confirmação:
    nome_arquivo_confirmacao = input(f"\nVc colocou pro arquivo chamar {nome_arquivo}.\nS para confirmar e n para negar: ").lower()
            # enquanto o usuário não digitar s (confirmar) o nome do arquivo, continuar perguntando o nome do arquivo e confirmação:
    while nome_arquivo_confirmacao != 's':
        nome_arquivo = input("\nInsira o nome do arquivo PDF que vc quer que o python salve\nCaso não tenha preferência, aperte enter, o Python vai salvar como pdf_merged.pdf. O arquivo será salvo na mesma pasta que vc indicou na pergunta anterior. ")
        if nome_arquivo == '':
            nome_arquivo_confirmacao = input(f"\nVc colocou pro arquivo chamar pdf_merged.pdf.\nS para confirmar e n para negar: ").lower()
        # caso o usuário digite qualquer coisa que não seja enter (independente se terminar com .pdf), pedir confirmação do nome inserido:
        elif nome_arquivo != '':
            if not nome_arquivo.endswith('.pdf'):
                nome_arquivo = nome_arquivo + '.pdf'
            nome_arquivo_confirmacao = input(f"\nVc colocou pro arquivo chamar {nome_arquivo}.\nS para confirmar e n para negar: ").lower()
    return nome_arquivo


# caso o usuário queira juntar apenas 1 pág de cada pdf, pergunta qual o nº da página:
def unica_pagina():
    pagina = int(input("\nDigite o nº da página dos PDFs que vc queira: "))
    # pedir confirmação da página que o usuário queira extrair:
    pagina_confirmacao = input(f"\nVc quer juntar a página nº {pagina} de cada um dos arquivos pdfs.\nS para confirmar e n para negar: ").lower()
    # enquanto o usuário não confirmar (s) a página, continuar perguntando a página e a confirmação:
    while pagina_confirmacao != 's':
        pagina = int(input("Digite o nº da página dos PDFs que vc queira: "))
        pagina_confirmacao = input(f"\nVc quer juntar a página nº {pagina} de cada um dos arquivos pdfs.\nS para confirmar e n para negar: ").lower()
    # quando o usuário confirmar, definir as páginas conforme o parametro do pypdf2 
    unica_pagina = (pagina-1, pagina)    
    return unica_pagina

# caso o usuário queira juntar uma sequência de pág de cada pdf, pergunta qual o nº inicial e o final da sequência:
def sequencia_paginas():
    primeira_pagina = int(input("Digite o nº da primeira página da sequência de páginas que vc queira: "))
    primeira_pagina_confirmacao = input(f"\n A primeira página a ser extraída será {primeira_pagina}.\nS pra confirmar e n pra negar: ").lower()
    while primeira_pagina_confirmacao != 's':
        primeira_pagina = int(input("Digite o nº da primeira página da sequência de páginas que vc queira: "))
        primeira_pagina_confirmacao = input(f"\n A primeira página a ser extraída será {primeira_pagina}.\nS pra confirmar e n pra negar: ").lower()

    ultima_pagina = int(input("Digite o nº da última página da sequência de páginas que vc queira: "))
    ultima_pagina_confirmacao = input(f"\n A última página a ser extraída será {ultima_pagina}.\nS pra confirmar e n pra negar: ").lower()
    while ultima_pagina_confirmacao != 's':
        ultima_pagina = int(input("Digite o nº da última página da sequência de páginas que vc queira: "))
        ultima_pagina_confirmacao = input(f"\n A última página a ser extraída será {ultima_pagina}.\nS pra confirmar e n pra negar: ").lower()
    
    # confirmada a sequencia a ser extraída, organizar em pages
    pages = (primeira_pagina, ultima_pagina)
    return pages


#______________________________________________________________________________________________________________________________
'''Abaixo estão as interações do python com o usuário:'''

instrucao = input('Caso queira instruções desse programa, digite s. Caso contrário, aperte enter: ').lower()
if instrucao == 's':
    terminou = input('''\nEsse comando só é válido se todos os PDFs que vc queira juntar estejam na mesma pasta. Eles não podem estar em subpastas.
Caso vc queira juntar PDFs que estejam em subpastas, eu fiz um outro programa pra isso. Execute-o e dps execute esse.
Quando eu pedir o caminho da pasta dos PDFs que vc queira juntar, cole o caminho com as barras pra direita -> C:/User/etc.
O PDF que o Python vai gerar vai ficar salvo na mesma pasta que estão os PDFs que vc quer juntar.\nAperte enter pra continuar: ''')

user_info = input('''\nSe vc quiser juntar todas as páginas do PDF, digite t.\nSe vc quiser partes dos PDFs, digite p: ''').lower()

# se o usuário quiser juntar todas as páginas dos PDFs:
if user_info == 't':
    diret = user_pasta()
    nome_arqv = user_nome_arqv()
    todo_pdf(diret, nome_arqv)


# se o usuário quiser juntar partes dos pdfs:
elif user_info == 'p':
    user_parte_pdf = input("\nVc quer juntar parte do PDF. Caso queira apenas 1 página de cada pdf, digite p. Caso queira uma sequência consecutiva de páginas, digite s: ")
    if user_parte_pdf == 'p':
        diret = user_pasta()
        nome_arqv = user_nome_arqv()
        one_page = unica_pagina()
        unica_pag(diret, one_page, nome_arqv)


# Caso o usuário queira uma sequência de pag de cada pdf:    
    elif user_parte_pdf == 's':
        diret = user_pasta()
        nome_arqv = user_nome_arqv()
        seq_pag = sequencia_paginas()
        sequencia_pag(diret, seq_pag, nome_arqv)

    else:
        print("\nEssa resposta não é válida. Vamos tentar de novo.")
else:
    print("\nEssa resposta não é válida. Vamos tentar de novo.")





