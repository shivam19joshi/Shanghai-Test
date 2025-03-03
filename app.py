import streamlit as st

st.set_page_config(page_title="Shanghai Stock Exchange", layout="wide")

st.markdown("<h1 style='text-align: center; background-color: lightred; padding: 10px; border-radius: 10px;'>SHANGHAI STOCK EXCHANGE</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'><u>INDEX</u></h3>", unsafe_allow_html=True)

stocks = [
    ["SYNOPEC_CORP", "CITIC", "SANY", "CMB"],
    ["PDH", "CHINA_UNICOM", "CSSC_HOLDINGS", "HENGRUI_PHARMA"],
    ["HAIER_SMART_HOME", "SHANXI_FEN_WINE", "YILI", "CYPC"],
    ["TONGWEI", "KWEICHOW_MOUTAI", "BANKCOMM", "CHINA_RAILWAY"]
]

cols = st.columns(4)
for row in stocks:
    for i, stock in enumerate(row):
        with cols[i]:
            if st.button(stock):
                st.session_state["selected_stock"] = stock
                st.switch_page(f"pages/{stock}.py") 


st.markdown("<p style='text-align: center;'>soham parsodkar</p>", unsafe_allow_html=True)
