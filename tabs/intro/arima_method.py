import streamlit as st
from tabs.tab import TabInterface


class IntroARIMA(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Arima]", divider="blue")
            st.markdown(
                """
                    ARIMA é uma plataforma de código aberto para aprendizado de máquina desenvolvida pelo Google. Ele oferece uma estrutura flexível e abrangente para construir e treinar modelos de aprendizado de máquina, utilizando tensores como sua estrutura básica de dados. TensorFlow é altamente escalável e adequado para uma ampla gama de aplicativos de aprendizado de máquina, desde reconhecimento de imagem até processamento de linguagem natural.
                """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                _, col0, _, col1, _ = st.columns([2, 2, 2, 2, 2])
