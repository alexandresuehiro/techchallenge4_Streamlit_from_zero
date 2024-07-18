import streamlit as st
#<<<<<<< HEAD
#
#st.title("🎈 My new app")
#st.write(
#    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
#)
#=======
from utils.constantes import TITULO_PRINCIPAL
from utils.layout import output_layout
import warnings



warnings.filterwarnings("ignore")

st.set_page_config(page_title=TITULO_PRINCIPAL, layout="wide")
output_layout()

st.header(f":orange[{TITULO_PRINCIPAL}]")

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(
    """
    Este trabalho tem por finalidade analisar o histórico de preços do petróleo Brent e criar modelos de machine learning que auxiliem na previsão do seu preço futuro. Para a realização deste trabalho, foi necessário analisar termos e fontes de dados para implementar processos de Machine Learning e exibi-los via Streamlit.
"""
)

st.subheader(
    ":blue[Sobre o petróleo Brent]",
    divider="blue",
)
st.markdown(
    """
    O Petróleo Brent é a referência internacional para os preços do petróleo, uma commodity muito valiosa por seu uso em geração de energia, transporte e outras finalidades.
Os valores históricos apresentados denotam que a geopolítica exerce grande influência ao causar grandes perturbações, por isso se torna crucial saber o comportamento do preço em situações extremamente críticas.
"""
)



st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """
    No primeiro momento, os dados históricos de preço do barril de petróleo Brent são consultados à partir de uma API da EIA (Energy Information Administration). Após a consulta, analisamos os dados para entender como os mesmos estão distribuidos.
    Com base na análise feita, são criados 2 modelos distintos que tem o intuito de prever o preço futuro do barril de petróleo.
    A respeito dos modelos criados:
    1. O primeiro modelo utiliza a biblioteca Prophet da Meta;
    2. O segundo modelo utiliza o algoritmo de rede neural LSTM (Long Short-Term Memory);
"""
)
#>>>>>>> f36f782 (Initial commit)
