import streamlit as st
import pandas as pd
import scipy.stats as stats

def calculate_pearson_correlation(groups):
    # Calculate Pearson correlation for each pair of groups
    correlations = []
    for i in range(len(groups)):
        for j in range(i+1, len(groups)):
            group1 = groups[i]
            group2 = groups[j]
            correlation, _ = stats.pearsonr(group1, group2)
            correlations.append((i+1, j+1, correlation))

    return correlations

def main():
    # Set title and description
    st.title("Pearson Correlation for Multiple Groups")
    st.write("Calculate Pearson correlation coefficient for multiple groups.")

    # Get the number of groups from the user
    num_groups = st.number_input("Enter the number of groups", min_value=2, step=1, value=2)

    # Create an empty list to store the data for each group
    groups = []

    # Take input for each group
    for i in range(num_groups):
        group_data = st.text_area(f"Enter data for Group {i+1} (comma-separated)", height=200)
        group_values = [float(value) for value in group_data.split(",") if value.strip()]
        groups.append(group_values)

    # Calculate Pearson correlation coefficients
    if st.button("Calculate Pearson Correlation"):
        correlations = calculate_pearson_correlation(groups)

        # Display the results
        st.write("Pearson Correlation Coefficients:")
        df = pd.DataFrame(correlations, columns=["Group 1", "Group 2", "Correlation"])
        st.dataframe(df)

# Run the app
if __name__ == "__main__":
    main()
