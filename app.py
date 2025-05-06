import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🖌️ Theme setup
sns.set(style="whitegrid", palette="pastel")

# 🎯 Title & intro
st.title("📊 Stock Close Price Visualizer")
st.markdown("""
Welcome to the **Interactive Stock Chart App**!  
Select a stock symbol below to explore its closing price trend over time.  
*Data. Charts. Clarity.* 🚀
""")

# 📁 Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("IFA.csv")  # Update this path if needed
    df = df.drop("Unnamed: 0", axis=1)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# 🔍 Stock selector
stock_list = sorted(df['Symbol'].unique())
selected_stock = st.selectbox("📌 Choose a stock:", stock_list)

# 🧾 Filter data
stk = df[df['Symbol'] == selected_stock]

# 📈 Plotting
st.subheader(f"📅 Close Price Trend for `{selected_stock}`")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=stk, x="Date", y="Close", ax=ax, marker="o")
ax.set_title(f"📉 Close Price over Time", fontsize=16)
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")
plt.xticks(rotation=45)
plt.tight_layout()

# 📷 Show plot
st.pyplot(fig)

# 📌 Footer
st.markdown("---")
st.caption("Made by Shivam")
