import pandas as pd
from process import ProcessadorTexto
import os

def processar_csv(caminho_entrada, caminho_saida):
    #nomes_colunas = ['target','ids','date','flag','user','text']
    colunas_mantidas = ['review_text', 'polarity']
    coluna_texto = 'review_text' 
    try:
        #chunks = pd.read_csv(caminho_entrada,header=None, names=nomes_colunas, sep=',', chunksize=10000, usecols=colunas_mantidas,encoding='ISO-8859-1')
        chunks = pd.read_csv(caminho_entrada, sep=',', chunksize=10000, usecols=colunas_mantidas,)
        processador = ProcessadorTexto()
        
        primeiro_chunk = True
        for chunk in chunks:
            print(f"📦 Processando lote de {len(chunk)} linhas...")
            
            # 2. Aplicar a limpeza na coluna de texto (ajuste o nome 'text' para o nome da sua coluna)
            # Supondo que a coluna de texto se chama 'review_text'
            #chunk['text_limpo'] = chunk[coluna_texto].apply(processador.limpar)
            textos_limpos = processador.limpar_lote(chunk[coluna_texto].tolist())
            chunk['text_limpo'] = textos_limpos
            
            # 3. Salvar o progresso (Append mode)
            chunk.to_csv(caminho_saida, index=False, mode='a', header=primeiro_chunk)
            primeiro_chunk = False
            
        print(f"✅ Sucesso! Arquivo limpo salvo em: {caminho_saida}")
        
    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")


if __name__ == "__main__":
    ENTRADA = "data/olist.csv"
    SAIDA = "data/trainingDT_limpo.csv"
    processar_csv(ENTRADA, SAIDA)
