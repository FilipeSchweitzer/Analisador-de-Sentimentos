import joblib
from process import ProcessadorTexto
import os

def carregar_ia():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    caminho_modelo = os.path.join(BASE_DIR, "modelo_sentimento.pkl")
    caminho_vetorizador = os.path.join(BASE_DIR, "vetorizador.pkl")

    print("Tentando carregar modelo de:", caminho_modelo)
    print("Existe?", os.path.exists(caminho_modelo))
    if not os.path.exists(caminho_modelo):
        caminho_modelo = os.path.join(BASE_DIR, "modelo_sentimento.pkl")
        caminho_vetorizador = os.path.join(BASE_DIR, "vetorizador.pkl")
    
    modelo = joblib.load(caminho_modelo)
    vectorizer = joblib.load(caminho_vetorizador)
    
    processador = ProcessadorTexto()
    
    return modelo, vectorizer, processador

def analisar_frase(frase, modelo, vectorizer, processador):

    frase_limpa = processador.limpar(frase)

    frase_tfindf = vectorizer.transform([frase_limpa])

    predicao = modelo.predict(frase_tfindf)[0]
    probabilidade = modelo.predict_proba(frase_tfindf).max()

    sentimento = "POSITIVO" if predicao == 1.0 else "NEGATIVO"

    print(f"\nFrase original: {frase}")
    print(f"Frase processada: {frase_limpa}")
    print(f"Resultado: {sentimento} (Confiança: {probabilidade:.2%})")

if __name__ == "__main__":
    print("--- Analisador de Sentimentos IA ---")
    modelo, vectorizer, processador = carregar_ia()
    while True:
        frase_user = input("\nDigite uma frase para analisar (ou 'sair): ")
        if frase_user.lower() == 'sair':
            break
        analisar_frase(frase_user, modelo, vectorizer, processador)
