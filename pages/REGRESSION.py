import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def perform_linear_regression(x, y):
    # Create a linear regression model
    model = LinearRegression()

    # Fit the model to the data
    model.fit(x, y)

    return model

def main():
    # Set title and description
    st.title("Simple Linear Regression")
    st.markdown('This app show you intercept and slope.')
    st.write("Perform simple linear regression.")

    # Get data from the user
    data = st.text_area("Enter data in CSV format (x, y)", height=200)

    # Parse the data into separate lists for x and y
    data_list = [row.split(",") for row in data.split("\n") if row.strip()]
    x = [float(row[0]) for row in data_list]
    y = [float(row[1]) for row in data_list]

    # Convert the lists to numpy arrays
    x = np.array(x).reshape(-1, 1)
    y = np.array(y)

    # Perform linear regression
    if st.button("Perform Linear Regression"):
        model = perform_linear_regression(x, y)

        # Display the regression results
        st.write("Regression Coefficients:")
        st.write(f"Intercept: {model.intercept_:.4f}")
        st.write(f"Slope: {model.coef_[0]:.4f}")


# Run the app
if __name__ == "__main__":
    main()
