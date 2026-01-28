import pandas as pd
import os

def carregar_dados():
    caminho_csv = os.path.join('data', 'trainingDT.csv')
    nomes_colunas = ['target','ids','date','flag','user','text']
    print("Carregando Arquivo...")
    if os.path.exists(caminho_csv):
        df = pd.read_csv(caminho_csv, header=None, names=nomes_colunas)
        print("Arquivo carregado com sucesso!")
        print("\nPrimeiras linhas do dataset:")
        print(df.head())
        return df
    else:
        print("Erro: O arquivo data/dados.csv não foi encontrado.")
        return None
    
if __name__ == "__main__":
    df_reviews = carregar_dados()
    #Tudo que não ajuda atrapalha 
    df_reviews = df_reviews.drop(columns=['ids', 'date', 'flag', 'user'])
    