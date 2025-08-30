import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Shipment Dashboard", layout="wide")

st.title("📦 Shipment Dashboard (Interactive)")

# Load cleaned data
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_shipments.csv")

try:
    df = load_data()
except:
    st.error("Please run ETL_shipment_pro.ipynb first to generate cleaned_shipments.csv")
    st.stop()

# KPIs
total = len(df)
delivered = (df['status'] == 'Delivered').sum()
claims = (df['status'] == 'Claimed').sum()
delivered_ratio = delivered / total * 100
claims_per_100 = claims / total * 100
avg_transit = (pd.to_datetime(df['delivered_date']) - pd.to_datetime(df['shipped_date'])).dt.days.mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Shipments", total)
col2.metric("Delivered Ratio", f"{delivered_ratio:.1f}%")
col3.metric("Claims per 100", f"{claims_per_100:.1f}")

st.metric("Avg Transit Days", f"{avg_transit:.1f}")

# Charts
st.subheader("📊 Shipments by Branch")
branch_counts = df['branch'].value_counts()
fig, ax = plt.subplots()
branch_counts.plot(kind="bar", ax=ax)
st.pyplot(fig)

st.subheader("📊 Status Distribution")
status_counts = df['status'].value_counts()
fig, ax = plt.subplots()
status_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax)
st.pyplot(fig)
