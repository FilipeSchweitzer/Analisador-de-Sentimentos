# Analisador de Sentimentos IA

Este projeto é uma solução completa de Processamento de Linguagem Natural (NLP) para classificação de sentimentos em avaliações de produtos e serviços. O modelo foi desenvolvido utilizando **Machine Learning** com foco em alta performance e escalabilidade, alcançando uma **acurácia de 92.2%**.

----------

## 🚀 Destaques do Projeto

-   **Acurácia Final:** 92.20% (F1-Score ponderado de 0.92).
    
-   **Interface Interativa:** Aplicação Web desenvolvida com Streamlit para predição em tempo real.
    
-   **Pipeline de NLP Profissional:** Limpeza de ruído, remoção de stopwords e lemmatização via SpaCy.
    
-   **Engenharia de Software:** Código modularizado em `src/`, testes unitários automatizados e gerenciamento de dependências.
    

----------

## 📊 Performance do Modelo

O modelo foi treinado utilizando **Logistic Regression** e vetorização **TF-IDF**, apresentando os seguintes resultados:

**Classe**

**Precisão**

**Recall**

**F1-Score**

**Negativo (0.0)**

0.86

0.88

0.87

**Positivo (1.0)**

0.95

0.94

0.94

**Geral (Média)**

**0.92**

**0.92**

**0.92**

----------

## 📁 Estrutura do Repositório

Plaintext

```
Analisador-de-Sentimentos/
├── data/               # Datasets (não versionados devido ao tamanho)
├── src/                # Código-fonte
│   ├── preprocessamento.py  # Lógica de limpeza de texto (NLP)
│   ├── treinar.py           # Script de treinamento do modelo
│   ├── predict.py           # Lógica de predição em tempo real
│   └── app_interface.py     # Interface Web (Streamlit)
├── tests/              # Testes unitários automatizados
├── modelo_sentimentos.pkl   # Modelo treinado (Cérebro da IA)
├── vetorizador.pkl          # Vetorizador TF-IDF persistido
├── pytest.ini               # Configuração do ambiente de testes
└── requirements.txt         # Dependências do projeto

```

----------

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3.13
    
-   **NLP:** SpaCy, NLTK
    
-   **Machine Learning:** Scikit-Learn
    
-   **Manipulação de Dados:** Pandas
    
-   **Interface:** Streamlit
    
-   **Testes:** Pytest
    

----------

## ⚙️ Como Executar o Projeto

### 1. Clonar e Configurar Ambiente

Bash

```
git clone https://github.com/FilipeSchweitzer/Analisador-de-Sentimentos.git
cd Analisador-de-Sentimentos
python -m venv venv
.\venv\Scripts\activate  # Windows

```

### 2. Instalar Dependências

Bash

```
pip install -r requirements.txt

```

### 3. Executar Testes Unitários

Bash

```
python -m pytest

```

### 4. Rodar a Interface Web

Bash

```
cd src
streamlit run app_interface.py

```

----------

## 👨‍💻 Sobre o Desenvolvedor

**Felipe Schweitzer** Estudante de Ciência de Dados e Inteligência Artificial no UniSenai Florianópolis.

Experiência em desenvolvimento de software e análise técnica, buscando aplicar IA para resolver problemas reais de negócio.