import streamlit as st

def perform_linear_regression(x, y):
    # Calculate the regression coefficients
    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n

    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    return intercept, slope

def main():
    # Set title and description
    st.title("Simple Linear Regression")
    st.markdown('This app shows the intercept and slope.')
    st.write("Perform simple linear regression.")

    # Get data from the user
    data = st.text_area("Enter data in CSV format (x, y)", height=200)

    # Parse the data into separate lists for x and y
    data_list = [row.split(",") for row in data.split("\n") if row.strip()]
    x = [float(row[0]) for row in data_list]
    y = [float(row[1]) for row in data_list]

    # Perform linear regression
    if st.button("Perform Linear Regression"):
        intercept, slope = perform_linear_regression(x, y)

        # Display the regression results
        st.write("Regression Coefficients:")
        st.write(f"Intercept: {intercept:.4f}")
        st.write(f"Slope: {slope:.4f}")

# Run the app
if __name__ == "__main__":
    main()
