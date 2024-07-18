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
import locale


warnings.filterwarnings("ignore")
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
st.set_page_config(page_title=TITULO_PRINCIPAL, layout="wide")
output_layout()

st.header(f":orange[{TITULO_PRINCIPAL}]")

st.subheader(
    ":blue[Análise histórica do petróleo Brent: analisando o seu passado e prevendo o seu futuro]",
    divider="blue",
)
st.markdown(
    """
    Este projeto tem como propósito analisar as flutuações históricas do preço do petróleo Brent e criar modelos de machine learning para prever seus valores futuros. O petróleo Brent, como uma referência internacional essencial para os preços do petróleo, é amplamente utilizado em transações comerciais e contratos futuros em âmbito global. Compreender as tendências passadas e identificar padrões nos dados históricos do preço do petróleo Brent oferece insights valiosos para investidores, empresas e formuladores de políticas energéticas.\n\n
    Ao explorar os dados históricos do preço do petróleo Brent, realizaremos análises estatísticas para compreender melhor os padrões e tendências ao longo do tempo. Este processo incluirá a identificação de fatores que influenciam significativamente o preço do petróleo, como oferta e demanda, geopolítica e condições econômicas globais. Além disso, utilizaremos técnicas de visualização de dados para destacar padrões e correlações relevantes, o que nos permitirá desenvolver insights mais aprofundados sobre o comportamento do mercado de petróleo.\n\n
    Após a análise, são criados dois modelo de machine learning voltados para séries temporais que serão responsáveis por prever o preço futuro do barril de petróleo Brent.
"""
)

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(
    """
    Analisar o histórico de preços do petróleo Brent e criar modelos de machine learning que auxiliem na previsão do seu preço futuro. Durante este projeto, também é abordado a questão de *deploy* de modelos num ambiente produtivo, no caso, esta aplicação Streamlit.
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
