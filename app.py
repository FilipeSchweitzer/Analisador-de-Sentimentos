import streamlit as st
import joblib
import os
from src.predict import carregar_ia, analisar_frase

st.set_page_config(page_title="IA Analisadora de Sentimentos", page_icon="🧠")

#@st.cache_resource

st.title("🧠 Analisador de Sentimentos IA")
st.markdown("Este projeto utiliza **Machine Learning** para classificar opiniões de usuários.")

modelo, vetorizador, processador = carregar_ia()

if modelo:
    texto_usuario = st.text_area("Digite um comentário sobre um produto ou serviço:", 
                                 placeholder="Ex: O produto chegou rápido e é de ótima qualidade!")
    
if st.button("Analisar Sentimento"):
    if texto_usuario:
        sentimento, probabilidade, texto_limpo= analisar_frase(texto_usuario, modelo, vetorizador, processador)

        st.divider()
        col1, col2 = st.columns(2)

        with col1:
            if sentimento == 'POSITIVO':
                st.success(f"### Sentimento: {sentimento}")
            else:
                st.error(f"### Sentimento: {sentimento}")
        with col2:
            st.metric("Confiança da IA", f"{probabilidade:.2%}")
        with st.expander("Ver detalhes do processamento técnico"):
            st.write(f"**Texto após limpeza (NLP):** {texto_limpo}")
            st.info("O modelo utiliza Regressão Logística com vetorização TF-IDF.")
    else:
        st.warning("Por favor, digite algum texto antes de analisar.")

st.sidebar.title("Sobre o Projeto")
st.sidebar.info("Desenvolvido por Felipe para demonstração técnica de IA.")