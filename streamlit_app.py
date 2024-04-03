
# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate random data for the scatter plot
np.random.seed(42)
n_points = 100
x_values = np.random.rand(n_points)
y_values = np.random.rand(n_points)

# Create a DataFrame from the random data
df = pd.DataFrame({'X': x_values, 'Y': y_values})

# Streamlit app layout
st.title("Simple Scatter Plot App")
st.write("This app displays a scatter plot using randomly generated data.")

# Display the scatter plot
# st.pyplot(plt.scatter(df['X'], df['Y']))
