import streamlit as st
import sympy as sp
import numpy as np


def trapezoidal_app():

    st.header("Trapezoidal Rule")

    x = sp.symbols('x')

    func_input = st.text_input(
        "Enter function f(x)",
        "x**2"
    )

    a = st.number_input(
        "Lower Limit (a)"
    )

    b = st.number_input(
        "Upper Limit (b)"
    )

    n = st.number_input(
        "Number of Intervals",
        min_value=1,
        value=4
    )

    if st.button("Calculate"):

        try:

            f = sp.lambdify(
                x,
                sp.sympify(func_input),
                "numpy"
            )

            h = (b - a) / n

            xs = np.linspace(
                a,
                b,
                int(n)+1
            )

            ys = f(xs)

            result = (
                h/2
                * (
                    ys[0]
                    + 2*sum(ys[1:int(n)])
                    + ys[int(n)]
                )
            )

            st.success(
                f"Integral Value = {round(result,4)}"
            )

        except:

            st.error(
                "Invalid function input"
            )
