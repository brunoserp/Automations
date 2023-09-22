# Verificar quais chaves NFe recebemos o XML
# Aperte F5 e fique atento ao terminal

input("Os arquivos devem estar salvos como .csv. Aperte enter: ")
import pandas as pd

# Definição do csv dos XMLs enviados e atribuição a um dataframe
xmls_enviados = input("Qual o diretório do csv com os XMLs enviados? ").replace('\\','/')
csv_enviados = pd.read_csv(xmls_enviados, header=None)
df_enviados = pd.DataFrame(csv_enviados)

# Definição do csv dos XMLs solicitados e atribuição a um dataframe
xmls_solicitados = input("Qual o diretório do csv com os XMLs solicitados? ").replace('\\','/')
csv_solicitados = pd.read_csv(xmls_solicitados, header=None)
df_solicitados = pd.DataFrame(csv_solicitados)

# Aqui cruza os dataframes e atribui True às chaves que recebemos
verificacao = df_solicitados.isin(df_enviados)
df_solicitados["Enviados?"] = verificacao

df_solicitados.to_csv(f"{xmls_solicitados[:-4]}_python{xmls_solicitados[-4:]}",index=False)
input("Pronto. O arquivo com os XMLs verificados foi salvo na mesma pasta do arquivo com os XMLs solicitados, porém com um '_python' no nome. Ele tá com a 1ª coluna com index (0,1,2,etc), pode excluir se quiser.")
