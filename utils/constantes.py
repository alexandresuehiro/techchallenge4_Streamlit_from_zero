import streamlit as st
from st_pages import show_pages, Page
import locale

from utils.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_HISTORIA, TITULO_INTRODUCAO, TITULO_MODELO, TITULO_REFLEXOES, TITULO_REFERENCIAS

def format_number(number, format='%0.0f'):
    return locale.format(format, number, grouping=True)

def output_layout():
    show_pages(
        [
            Page("./main.py", "Tech Challenge 4", use_relative_hash=True),                  # ":house:", use_relative_hash=True),
            Page("./pages/intro.py", TITULO_INTRODUCAO, use_relative_hash=True),            #":books:", use_relative_hash=True),
            Page("./pages/historia.py", TITULO_HISTORIA, use_relative_hash=True),           #":open_book:", use_relative_hash=True),
            Page("./pages/analise.py", TITULO_ANALISE_EXPLORATORIA, use_relative_hash=True),#":memo:", use_relative_hash=True),
            Page("./pages/modelo.py", TITULO_MODELO, use_relative_hash=True),               #":robot_face:", use_relative_hash=True),
            Page("./pages/reflexoes.py", TITULO_REFLEXOES, use_relative_hash=True),         #":robot_face:", use_relative_hash=True),
            Page("./pages/refs.py", TITULO_REFERENCIAS, use_relative_hash=True)             #":globe_with_meridians:", use_relative_hash=True),
        ]
    )

    with st.sidebar:
        st.subheader("Aluno")
        st.text("Alexandre Suehiro de Paula e Silva")
        st.text("RM 352798 - 3DTAT")

        st.divider()

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

        st.divider()

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