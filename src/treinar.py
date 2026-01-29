import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

def treinar():
    print("Carregando dados limpos...")
    df = pd.read_csv('../data/trainingDT_limpo.csv').dropna()

    x = df['text_limpo']
    y = df['polarity']

    # dividir 80% para treinar e 20% para testar
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Texto para numero
    print("Vetorizando texto...")
    vectorizer = TfidfVectorizer(max_features=5000)
    x_train_tfidf = vectorizer.fit_transform(x_train)
    x_test_tfidf = vectorizer.transform(x_test)

    print("Treinando o modelo de IA...")
    modelo = LogisticRegression()
    modelo.fit(x_train_tfidf, y_train)

    y_pred = modelo.predict(x_test_tfidf)
    print("\n--- Relatório de Performance ---")
    print(f"Acurácia: {accuracy_score(y_test, y_pred):.2%}")
    print(classification_report(y_test,y_pred))

    print("Salvando modelo...")
    joblib.dump(modelo, 'modelo_sentimento.pkl')
    joblib.dump(vectorizer, 'vetorizador.pkl')
    print('Tudo pronto!')

if __name__ == "__main__":
    treinar()