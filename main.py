import streamlit as st

# Import methods
from methods.gauss_seidel import gauss_seidel_app
from methods.milne_method import milne_app
from methods.trapezoidal_rule import trapezoidal_app


st.set_page_config(
    page_title="Numerical Methods Solver",
    layout="centered"
)

st.title("Numerical Methods Calculator")

method = st.sidebar.selectbox(
    "Choose Method",
    (
        "Gauss-Seidel",
        "Milne Method",
        "Trapezoidal Rule"
    )
)

if method == "Gauss-Seidel":
    gauss_seidel_app()

elif method == "Milne Method":
    milne_app()

elif method == "Trapezoidal Rule":
    trapezoidal_app()
