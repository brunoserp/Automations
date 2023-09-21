# Verificar quais chaves NFe recebemos o XML
# Aperte F5 e fique atento ao terminal

input("Os arquivos devem estar salvos como .csv e as células A1 devem estar escritas Col1. Aperte enter")
import pandas as pd

# Definição do csv dos XMLs enviados e atribuição a um dataframe
xmls_enviados = input("Qual o diretório do csv com os XMLs enviados? ").replace('\\','/')
csv_enviados = pd.read_csv(xmls_enviados)
df_enviados = pd.DataFrame(csv_enviados)

# Definição do csv dos XMLs solicitados e atribuição a um dataframe
xmls_solicitados = input("Qual o diretório do csv com os XMLs solicitados? ").replace('\\','/')
csv_solicitados = pd.read_csv(xmls_solicitados)
df_solicitados = pd.DataFrame(csv_solicitados)

# Aqui cruza os dataframes e atribui True às chaves que recebemos
verificacao = df_solicitados["Col1"].isin(df_enviados["Col1"])
df_solicitados["Enviados?"] = verificacao

df_solicitados.to_csv(xmls_solicitados)
input("Pronto. O arquivo com os XMLs solicitados foi substituído.")
