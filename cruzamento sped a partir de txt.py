# baixe o arquivo "Registro e Campos - EFD ICMS IPI e Contribuições.xlsx" numa pasta e coloque o caminho da pasta na variável pasta dentro da def selecao_registro

import csv
import os
import pandas as pd
from pathlib import Path

def selecao_registro(registro,tipo):
    lista=[]
    pasta = r"C:\Users\bserpellone\Documents\Projetos\Planilhas dimensão CFOP, UF, CST"
    arquivo = "Registro e Campos - EFD ICMS IPI e Contribuições.xlsx"
    if tipo == 'ICMS':
        df = pd.read_excel(os.path.join(pasta,arquivo),sheet_name='Campos - EFD ICMS IPI',header=3)
    elif tipo == 'Contribuições':
        df = pd.read_excel(os.path.join(pasta,arquivo),sheet_name='Campos -  EFD Contribuições',header=3)
    df = df[df['Registro'].str.lower()==registro]
    df.dropna(axis=1,inplace=True)
    return df.iloc[0,3:].to_list() 
    # return [f"{registro.upper()}_" + str(valor).upper() for valor in df.iloc[0, 3:].to_list()] # pra adicionar prefixo do registro no cabeçalho. Ex C100_CHV_NFE (comente a linha acima)


def read_file(file_path):
    try:
        with open(file_path, 'r', newline='\n', encoding='utf-8') as txtfile:
            return txtfile.readlines()
    except UnicodeDecodeError:
        with open(file_path, 'r', newline='\n', encoding='ANSI') as txtfile:
            return txtfile.readlines()

print('\n')

base_directory = Path(input("Insira a pasta que estão os txt >>> "))
tipo_txt = input('É EFD ICMS ou Contribuições? (i/c) >>> ').lower()
if tipo_txt == 'i':
    tipo_txt = 'ICMS'
elif tipo_txt == 'c':
    tipo_txt = 'Contribuições'

# lista para armazenar os dados filtrados
filtered_data = []

registro_pai = input("Indique o registro pai desejado: ").title()
registro_filho = input("Indique o registro filho desejado: ").title()
registro_valido = (registro_pai if registro_filho == '' else registro_filho if registro_pai == '' else None)
print('\n >>> Acessando os arquivos')
contador = {}
qtd_total = 0
for foldername, subfolders, filenames in os.walk(base_directory):
    qtde = 0
    for filename in filenames:
        if filename.endswith('.txt'):
            file_path = os.path.join(foldername, filename).replace('\\', '/')
            lines = read_file(file_path)
            print(f"{filename}")
            
            if registro_valido is None:
                qtde +=1

                current_pai = None  # Variável para armazenar o último registro-pai lido

                for line in lines:
                    if line.startswith(f'|{registro_pai}|'):
                        current_pai = line.strip().split('|')[1:-1]  # Armazenar as colunas do registro-pai atual, sem o |nº registro|
                    elif line.startswith(f'|{registro_filho}|') and current_pai is not None:
                        columns_filho = line.strip().split('|')[1:-1]  # Obter as colunas do registro filho
                        combined_row = current_pai + columns_filho  # Concatenar as colunas do pai e filho
                        filtered_data.append(combined_row)
            
            else: # caso seja só 1 registro, sem cruzamento
                for line in lines:
                    if registro_filho == '' and line.startswith(f'|{registro_pai}|'):
                        filtered_data.append(line.strip().split('|')[1:-1])    
                    elif registro_pai == '' and line.startswith(f'|{registro_filho}|'):
                        filtered_data.append(line.strip().split('|')[1:-1])
            
            qtd_total += len(filtered_data)
            print(f'   Qtd linhas do arquivo: {len(filtered_data):,}'.replace(',', '.'))
            print(f'   Qtd linhas acumuladas: {qtd_total:,}'.replace(',', '.'))

filtered_data = list(filtered_data)
df = pd.DataFrame(filtered_data)

if registro_filho == '':
    lista_cabecalho = selecao_registro(str(registro_pai).lower(),tipo_txt)
elif registro_pai == '':
    lista_cabecalho = selecao_registro(str(registro_filho).lower(),tipo_txt)
else:
    lista_cabecalho=selecao_registro(registro_pai.lower(),tipo_txt) + selecao_registro(str(registro_filho).lower(),tipo_txt)

df.columns = lista_cabecalho

if df.shape[0] < 1000000:
    df.to_excel(os.path.join(base_directory,f'{registro_pai}_{registro_filho}.xlsx'),index=None)
else:
    df.to_csv(os.path.join(base_directory,f'{registro_pai}_{registro_filho}.csv'),index=None)

