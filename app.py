import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Title
st.title("Stock Close Price Visualization")

# Load Data
df = pd.read_csv("IFA.csv")
df = df.drop("Unnamed: 0", axis=1)
df['Date'] = pd.to_datetime(df['Date'])

# Stock Selection
stock_list = df['Symbol'].unique()
selected_stock = st.selectbox("Select Stock Symbol:", stock_list)

# Filter Data
stk = df[df['Symbol'] == selected_stock]

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
sb.lineplot(data=stk, x="Date", y="Close", ax=ax)
plt.xticks(rotation=90)
plt.title(f"Close Price Trend for {selected_stock}")
st.pyplot(fig)
