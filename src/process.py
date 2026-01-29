import re
import nltk
import spacy
from nltk.corpus import stopwords


nltk.download('stopwords')
nlp = spacy.load('pt_core_news_sm', disable=['ner', 'parser'])

class ProcessadorTexto:
    def __init__(self):
        self.stop_words = set(stopwords.words('portuguese'))
        self.re_url = re.compile(r"https?://\S+|http\S+|www\S+|@\w+")
        self.re_limpeza = re.compile(r"[^a-záàâãéèêíïóôõöúçñ ]")
    
    def limpar(self, texto) -> str:
        texto = str(texto).lower()
        texto = self.re_url.sub(" ", texto)
        #texto = re.sub(r'<.*?>', ' ', texto)
        texto = self.re_limpeza.sub(" ", texto)
        doc = nlp(texto)
        tokens = [token.lemma_ for token in doc if token.text not in self.stop_words]
        
        return " ".join(tokens).strip()
    
    def limpar_lote(self, lista_textos):
        # nlp.pipe processa os textos em paralelo internamente
        docs = nlp.pipe(lista_textos, batch_size=1000, disable=["ner", "parser"])
        
        textos_processados = []
        for doc in docs:
            # Mesma lógica de limpeza, mas aproveitando o processamento em lote
            tokens = [token.lemma_ for token in doc if token.text not in self.stop_words and not token.is_space]
            textos_processados.append(" ".join(tokens).strip())
            
        return textos_processados
    
if __name__ == "__main__":
    processador = ProcessadorTexto()
    exemplo = "Eu adorei o produto! @vendedor, chegou muito rápido. 😊 link: http://loja.com"
    print(f"Original: {exemplo}")
    print(f"Limpo: {processador.limpar(exemplo)}")