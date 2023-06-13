import streamlit as st
import pandas as pd
import scipy.stats as stats

def one_way_anova(groups):
    # Perform one-way ANOVA test
    statistic, p_value = stats.f_oneway(*groups)
    return statistic, p_value

def main():
    # Set title and description
    st.title("One-Way ANOVA Test")
    st.write("Perform a one-way ANOVA test.")

    # Get the number of groups from the user
    num_groups = st.number_input("Enter the number of groups", min_value=2, step=1, value=2)

    # Create an empty list to store the data for each group
    groups = []

    # Take input for each group
    for i in range(num_groups):
        group_data = st.text_input(f"Enter data for Group {i+1} (comma-separated)")
        # Split the input and convert it to a list of numbers if it's not empty
        if group_data:
            group_values = list(map(float, group_data.split(",")))
            groups.append(group_values)

    # Perform the one-way ANOVA test
    if st.button("Perform ANOVA Test") and len(groups) == num_groups:
        statistic, p_value = one_way_anova(groups)
        st.write("ANOVA Results:")
        st.write(f"Statistic: {statistic:.2f}")
        st.write(f"p-value: {p_value:.4f}")
    elif len(groups) != num_groups:
        st.warning("Please provide data for all groups.")

# Run the app
if __name__ == "__main__":
    main()
