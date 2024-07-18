import streamlit as st
from utils.constantes import TITULO_PRINCIPAL, TITULO_REFERENCIAS
from utils.layout import output_layout

from utils.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_HISTORIA, TITULO_INTRODUCAO, TITULO_MODELO, TITULO_REFLEXOES, TITULO_REFERENCIAS

def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

with st._main:

        st.subheader("Como construir o app?")
        st.text("Do zero, no site do streamlit")
        st.text("Acessar o 'Create app' - 'Blank App'")
        
        st.subheader("Como construir o app (localmente)?")
        st.text("Criar ambiente com Virtualenv")
        st.code(body="python -m venv venv", language="shell")
        st.code(body="source venv/Scripts/activate", language="shell")
        st.code(body="pip install -r requirements.txt", language="shell")
        st.subheader("Executar localmente")
        st.code(body="streamlit run main.py", language="shell")

        st.subheader("Repositórios do projeto")
        st.link_button(
            "Repositório Streamlit",
            "https://github.com/dhachcar/postech-tech-challenge-4-streamlit",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )
        st.link_button(
            "Repositório Jupyter Notebook",
            "https://github.com/alexandresuehiro/Postgrad_FIAP_3DTAT/tree/main/techchallenge-4",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )