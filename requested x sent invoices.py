'''
RESUMO:
Esse programa confere se os XML solicitados foram enviados
Vc deve responder algumas perguntas pra ele conferir: se vc tem um csv com a lista de chaves do C100 (solicitadas) e a lista de xml enviados,
caso contrário, ele tem a funcionalidade de vc passar o caminho da pasta com os txt (eles devem estar deszipados e explícitos na pasta,
o programa não entra em subpastas pra procurar txt) e compilar as chaves (C100_CHV_NFE), e tbm a funcionalidade de fazer uma lista com os XML enviados.
Ainda, caso o usuário confirme, ele salva a lista com XML enviados, solicitados (C100_CHV_NFE válidos), e dos XML que ainda permanecem pendentes


Pra selecionar as colunas do C100 que vc queira salvar junto com a conferência, mude:
df_solicitados = (df_solicitados.iloc[:,[6,8,9,10,11]])
-> indique os números dos campos que vc queira (veja no manual EFD, o 6 por exemplo é o COD_SIT)
df_solicitados.columns=['COD_SIT','NUM_DOC','CHV_NFE','DT_DOC','DT_E_S']
-> indique o NOME dessas colunas selecionadas por números (os nomes tem que ser nas ordens dos números)
'''

import pandas as pd
import os
import zipfile
import io

#________________________________________________________________________________________________________________________________
# Função p/ importar as chaves dos TXT e empilhar num dataframe:
#________________________________________________________________________________________________________________________________
def importar_sped_txt():
    pasta_txt = input("Insira a pasta que tenha os txt deszipados >>> ")
    arquivos_pasta = os.listdir(pasta_txt)
    lista = []
    for raiz, pastas, arquivos in os.walk(pasta_txt):
        for arquivo in arquivos:
            if arquivo.endswith('.txt'):
                with open(os.path.join(pasta_txt,arquivo), encoding='ANSI') as arqv:
                    for linhas in arqv:
                        if linhas.startswith('|C100|'):
                            lista.append(linhas)
            
            elif arquivo.endswith('.zip'):
                print(f"    Analisando o arquivo zip: {arquivo}")
                caminho_zip = os.path.join(raiz, arquivo)
                print(f"caminho_zip: {caminho_zip}")
                with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                    for file in zip_ref.namelist():
                        if file.lower().endswith('.zip'):
                            print(f"        Acessando o zip {file}")
                            # Se o arquivo for um zip, extraia os txt
                            inner_zip_content = zip_ref.read(file)
                            with zipfile.ZipFile(io.BytesIO(inner_zip_content)) as inner_zip_ref:
                                for inner_file in inner_zip_ref.namelist():
                                    if inner_file.lower().endswith('.txt'):
                                        with open(os.path.join(raiz,arquivo), encoding='ANSI') as arqv:
                                            for linhas in arqv:
                                                if linhas.startswith('|C100|'):
                                                    lista.append(linhas)
                        elif file.lower().endswith('.txt'):
                            with zip_ref.open(file) as arqv:
                                with io.TextIOWrapper(arqv, encoding='ANSI') as arqv_decodificado:
                                    for linhas in arqv_decodificado:
                                        if linhas.startswith('|C100|'):
                                            lista.append(linhas)
    
    df_solicitados = pd.DataFrame(lista,dtype=str)
    print(df_solicitados.head(5))
    df_solicitados = df_solicitados.iloc[:,0].str.split('|',expand=True)
    df_solicitados = (df_solicitados.iloc[:,[6,8,9,10,11]])
    df_solicitados.columns=['COD_SIT','NUM_DOC','CHV_NFE','DT_DOC','DT_E_S']
    df_solicitados.drop_duplicates(inplace=True)
    df_solicitados_validos = df_solicitados[~df_solicitados['COD_SIT'].isin(['02','03','04','05'])]

    confirmacao_salvar_lista_chaves = input("Quer salvar um arquivo em Excel com as chaves das NF do SPED empilhadas? (s/n) >>> ")
    if confirmacao_salvar_lista_chaves.lower() == 's':
        df_solicitados_validos.to_excel(os.path.join(pasta_txt,'C100_CHV_NFE_empilhado.xlsx'),index=False)
        print(f"O arquivo foi salvo na pasta {os.path.join(pasta_txt,'C100_CHV_NFE_validos_empilhados.xlsx')}")
    return df_solicitados_validos

#________________________________________________________________________________________________________________________________
# Função p/ listar os XML enviados e empilhar num dataframe:
#________________________________________________________________________________________________________________________________
def lista_xml():
    pasta_enviados = input("Insira a pasta com os XML >>> ")
    xml_set = set()
    dict_qtde = {}
    qtd_total = 0

    for raiz, pastas, arquivos in os.walk(pasta_enviados):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.xml'):
                caminho_arquivo = os.path.join(raiz, arquivo)
                xml_set.add(arquivo[:44])
                qtd_total += 1
        for arquivo in arquivos:
            if arquivo.lower().endswith('.zip'):
                print(f"    Analisando o arquivo zip: {arquivo}")
                caminho_zip = os.path.join(raiz, arquivo)
                qtde_zip = 0
                with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
                    for file in zip_ref.namelist():
                        if file.lower().endswith('.zip'):
                            print(f"        Acessando o zip {file}")
                            # Se o arquivo for um zip, extraia os XMLs recursivamente
                            inner_zip_content = zip_ref.read(file)
                            with zipfile.ZipFile(io.BytesIO(inner_zip_content)) as inner_zip_ref:
                                for inner_file in inner_zip_ref.namelist():
                                    if inner_file.lower().endswith('.xml'):
                                        caminho_xml = os.path.join(raiz, arquivo, inner_file)
                                        lista_arquivo = inner_file.split('/')
                                        chave = lista_arquivo[-1]
                                        xml_set.add(chave[:44])
                                        qtde_zip += 1
                                        qtd_total += 1
                        elif file.lower().endswith('.xml'):
                            caminho_xml = os.path.join(raiz, arquivo, file)
                            lista_file = file.split('/')
                            chave_nf = lista_file[-1]
                            xml_set.add(chave_nf[:44])
                            qtde_zip += 1
                            qtd_total += 1

                dict_qtde[arquivo] = qtde_zip

    print("Quantidade de XML enviados:", qtd_total)
    print("     Quantidade de XML DISTINTOS enviados:", len(xml_set))
    print("\nQuantidade de arquivos XML enviados em cada arquivo zip:")
    for zip_file, qtde in dict_qtde.items():
        print(f"{zip_file}: {qtde}")
    
    dicionario_enviados = {'enviados': list(xml_set)}
    df_enviados = pd.DataFrame(dicionario_enviados)
    return df_enviados

#________________________________________________________________________________________________________________________________
# Função p/ confrontar confrontar os XML enviados x chaves solicitadas:
#________________________________________________________________________________________________________________________________
def confronto_pendentes_x_enviados(df_solicitados, df_enviados):
    df_solicitados_que_foram_enviados = df_solicitados[df_solicitados['CHV_NFE'].isin(df_enviados['enviados'])]
    df_solicitados_n_enviados = df_solicitados[~df_solicitados['CHV_NFE'].isin(df_enviados['enviados'])]
    print(f"Dos {len(df_solicitados)} XML solicitados, {len(df_solicitados_que_foram_enviados)} foram enviados")
    print(f"Ainda há {len(df_solicitados_n_enviados)} XML pendentes")
    
    salvar_enviados = input("\nVc quer salvar num Excel todos os XML enviados? (s/n) >>> ")
    if salvar_enviados.lower() == 's':
        pasta_enviados = input("    Insira a pasta p/ salvar um Excel com os XML enviados >>> ")
        df_enviados.to_excel(os.path.join(pasta_enviados,'enviados.xlsx'),index=False)

    salvar_n_enviados = input("\nVc quer salvar um Excel com os XML solicitados que não foram enviados? (s/n) >>> ")
    if salvar_n_enviados.lower() == 's':
        pasta_n_enviados = input("    Insira a pasta que queira salvar esse Excel >>> ")
        df_solicitados_n_enviados.to_excel(os.path.join(pasta_n_enviados,"xml_pendentes.xlsx"),index=False)
        print(f"Excel salvo em   {os.path.join(pasta_n_enviados,'xml_pendentes.xlsx')}")

#________________________________________________________________________________________________________________________________

# 1º: obter um dataframe com os XML solicitados:
lista_chaves_sped = input('''
>>> XML solicitados:
    1) Eu tenho um csv com todas as chaves empilhadas na primeira coluna e sem cabeçalho
    2) Eu tenho apenas os txt do SPED e quero empilhar as chaves de todos esses arquivos \n
    Indique o número entre os 2 acima pra prosseguir >>>
    ''')

if lista_chaves_sped == '1':
    pasta_csv = input("Insira o caminho da pasta que tenha o CSV com os XML solicitados. Não esqueça de colocar o nome do CSV no final >>> ")
    if not pasta_csv.lower().endswith('.csv'):
        pasta_csv += '.csv'
    lista_solicitados = pd.read_csv(pasta_csv)
elif lista_chaves_sped == '2':
    lista_solicitados = importar_sped_txt()


# 2º: obter um dataframe com os XML enviados:
lista_xml_enviados = input('''
>>> XML enviados:
    1) Eu tenho um csv com todos os XML recebidos
    2) Eu tenho apenas os XML numa pasta (tanto zipado quanto deszipado) \n
    Indique o número entre os 2 acima pra prosseguir >>>
    ''')

if lista_xml_enviados == '1':
    pasta_csv = input("Insira o caminho da pasta que tenha o CSV com os XML enviados. Não esqueça de colocar o nome do CSV no final >>> ")
    if not pasta_csv.lower().endswith('.csv'):
        pasta_csv += '.csv'
    lista_enviados = pd.read_csv(pasta_csv)
elif lista_chaves_sped == '2':
    lista_enviados = lista_xml()


# 3°: confrontar se os XML solicitados foram enviados:
print(">>> Confrontar XML solicitados x enviados:")
confronto_pendentes_x_enviados(lista_solicitados,lista_enviados)
