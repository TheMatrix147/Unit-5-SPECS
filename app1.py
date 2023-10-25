import streamlit as st
import pandas as pd
import numpy as np


st.title("Derek's Store - Admin Dashboard")

df = pd.read_csv("supermarket.csv")

st.subheader('Top 10 Performing Stores')
top_stores = pd.DataFrame(data=df.groupby(by='store_id')['store_sales'].sum()).sort_values(by='store_sales', ascending=False).head(10)
st.bar_chart(data = top_stores)

st.subheader('Average Store Sales Overall')
avg_store_sales = round(np.mean(df['store_sales']))
st.markdown(f'<h1 style="color:#4dd906;font-size:50px">{avg_store_sales}</h1>', unsafe_allow_html=True)

st.markdown('<h3 style="color:#d92906">Lowest 10 Performing Stores</h3>', unsafe_allow_html=True)
lowest_stores = pd.DataFrame(data=df.groupby(by='store_id')[['store_id','store_sales']].sum()).sort_values(by='store_sales', ascending=True).head(10)
st.table(data = lowest_stores)
