# Verificar quais chaves NFe recebemos o XML
# Aperte F5 e fique atento ao terminal

print("Os arquivos devem estar salvos como .csv")

import pandas as pd
import os

arquivo_final = input("Insira o caminho da pasta que vc quer salvar o arquivo final: ").replace('\\','/')
if not arquivo_final.endswith('/'):
    arquivo_final = arquivo_final + '/'

# Função para ler os arquivos CSV e criar DataFrames
def read_csv_to_dataframe():
    file_paths = []
    while True:
        file_path = input("Insira o caminho do arquivo do CSV (ou 'q' para sair): ").strip()
        if file_path == 'q':
            break
        if os.path.exists(file_path):
            file_paths.append(file_path)
        else:
            print(f"Arquivo não encontrado: {file_path}")
# Nessa parte acima ele coleta os arquivos do usuário e adiciona numa lista

    dataframes = []
    for file_path in file_paths:
        csv_data = pd.read_csv(file_path, header=None)
        df = pd.DataFrame(csv_data)
        dataframes.append(df)
# Nessa parte acima ele pega cada arquivo inserido pelo usuário e cria um dataframe, e tbm cria uma lista com o nome de cada dataframe 
    
    if len(dataframes) == 0:
        return None
    elif len(dataframes) == 1:
        return dataframes[0]
    else:
        return pd.concat(dataframes, ignore_index=True)
# Por fim, se a lista tiver 1 dataframe, a função retorna o 1º (e único) dataframe. Se tiver mais, ele empilha um embaixo do outro

# Ler os XMLs enviados
print("XMLs Enviados:")
lista_de_XML_enviados = read_csv_to_dataframe()

# Ler os XMLs solicitados
print("XMLs Solicitados:")
lista_de_XML_solicitados = read_csv_to_dataframe()

# Acima ele usa a função definida anteriormente. Note que a função é feita de forma abrangente pra abrangir tanto os XMLs enviados, quanto os XMLs solicitados

if lista_de_XML_enviados is not None and lista_de_XML_solicitados is not None:
# Verificar quais chaves NFe recebemos o XML (o [0] indica a coluna)
    verificacao = lista_de_XML_solicitados[0].isin(lista_de_XML_enviados[0])
    
# Filtrar apenas as linhas de XMLs solicitados que não têm correspondência (o ~indica inversão. Ou seja, no código logo acima ele atribuiu True pros XMLs
# solicitados que estão na lista de xmls enviados, e False caso contrário. Nessa linha debaixo ele vai inverter esses True / False)
    lista_de_XML_solicitados_sem_correspondencia = lista_de_XML_solicitados[~verificacao]

    if not lista_de_XML_solicitados_sem_correspondencia.empty:
        batch_size = 1000000
        num_batches = len(lista_de_XML_solicitados_sem_correspondencia) // batch_size + 1
# esse num_batches acima seria a qtde de arquivos que o python vai gerar (1mi linhas por arquivo)
        for i in range(num_batches):
            start = i * batch_size
            end = (i + 1) * batch_size
            df_batch = lista_de_XML_solicitados_sem_correspondencia[start:end]
            output_filename = f"{arquivo_final}conferencia_python_{i + 1}.xlsx"
            df_batch.to_excel(output_filename, index=False)
        
        print(f"O arquivo com os XML pendentes (conferencia_python.xlsx) foi salvo em {arquivo_final}.")
    else:
        print("Todos os XMLs solicitados foram enviados")
else:
    print("Nenhum arquivo válido foi fornecido.")
