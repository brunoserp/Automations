import pandas as pd
import os

# Include folder + file names inside the quotation marks below
pasta = r''

for file in os.listdir(pasta):
    if file.endswith('relat_xml.csv'):
        print(f'>>>> {file}')
        caminho = os.path.join(pasta,file)
        df = pd.read_csv(caminho,delimiter='|',encoding='ANSI',dtype=str)
        for col in df.columns.values:
            if '/' in col or ' ' in col or '-' in col or '.' in col:
                print(f'[{col}] varchar(50),')
            else:
                print(f'{col} varchar(50),')
        print('-----------------------------------------------')
