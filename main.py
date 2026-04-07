import streamlit as st

from methods.gauss_seidel import gauss_seidel_app
from methods.trapezoidal_rule import trapezoidal_app
from methods.milne_method import milne_app


st.set_page_config(
    page_title="Numerical Methods Calculator",
    page_icon="📐",
    layout="wide"
)

st.title("📐 Numerical Methods Smart Calculator")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Method",
    [
        "Gauss Seidel Method",
        "Trapezoidal Rule",
        "Milne Predictor Corrector"
    ]
)

if page == "Gauss Seidel Method":
    gauss_seidel_app()

elif page == "Trapezoidal Rule":
    trapezoidal_app()

elif page == "Milne Predictor Corrector":
    milne_app()
