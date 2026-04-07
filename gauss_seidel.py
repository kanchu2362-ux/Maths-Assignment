import streamlit as st
import numpy as np
import pandas as pd


def gauss_seidel_app():

    st.header("Gauss-Seidel Method")

    n = st.number_input(
        "Number of Variables",
        min_value=2,
        max_value=5,
        value=3
    )

    st.write("Enter coefficients row-wise")

    # Default Example Matrix
    default_rows = [
        "10 -1 2",
        "-1 11 -1",
        "2 -1 10"
    ]

    A = []

    for i in range(n):

        row = st.text_input(
            f"Row {i+1}",
            value=default_rows[i]
            if i < len(default_rows)
            else ""
        )

        if row:

            values = [
                float(x)
                for x in row.split()
            ]

            if len(values) != n:
                st.error(
                    f"Row must contain {n} values"
                )
                return

            A.append(values)

    # Default values
    b_input = st.text_input(
        "Constant Terms (b)",
        value="6 25 -11"
    )

    x0_input = st.text_input(
        "Initial Guess",
        value="0 0 0"
    )

    tol = st.number_input(
        "Tolerance",
        value=0.0001,
        format="%.6f"
    )

    max_iter = st.number_input(
        "Maximum Iterations",
        value=25
    )

    if st.button("Solve"):

        try:

            if len(A) != n:
                st.error(
                    "Enter all rows"
                )
                return

            A = np.array(A)

            b = np.array([
                float(i)
                for i in b_input.split()
            ])

            x = np.array([
                float(i)
                for i in x0_input.split()
            ])

            iterations = []

            for k in range(int(max_iter)):

                x_new = np.copy(x)

                for i in range(n):

                    s1 = sum(
                        A[i][j] * x_new[j]
                        for j in range(i)
                    )

                    s2 = sum(
                        A[i][j] * x[j]
                        for j in range(i+1, n)
                    )

                    x_new[i] = (
                        b[i]
                        - s1
                        - s2
                    ) / A[i][i]

                error = np.linalg.norm(
                    x_new - x,
                    ord=np.inf
                )

                iterations.append(
                    [k+1]
                    + [round(float(val),4) for val in x_new]
                    + [round(float(error),6)]
                )

                x = x_new

                if error < tol:
                    break

            columns = (
                ["Iteration"]
                + [f"x{i+1}" for i in range(n)]
                + ["Error"]
            )

            df = pd.DataFrame(
                iterations,
                columns=columns
            )

            st.subheader("Iteration Table")

            st.dataframe(df)

            # ✅ Final Solution Formatting (FIXED)

            solution = [
                f"{float(val):.4f}"
                for val in x
            ]

            st.success(
                f"Final Solution: {solution}"
            )

        except:

            st.error(
                "Invalid input values"
            )
