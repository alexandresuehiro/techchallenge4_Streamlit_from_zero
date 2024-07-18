import streamlit as st
from utils.constantes import TITULO_PRINCIPAL, TITULO_REFERENCIAS
from utils.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_PRINCIPAL} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_PRINCIPAL}]")

    st.markdown(
        """
        Nesta introdução, são descritos alguns tópicos importantes para o entendimento do projeto, dentre eles oque é o petróleo Brent, a EIA e o IPEA.
    """
    )

