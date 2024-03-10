import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

all_df = pd.read_csv("product_report_data.csv")

def purchased_per_city(df):
    return df.groupby('customer_city')['price'].sum().reset_index(name='total').sort_values(by='total', ascending=False)

def purchased_per_state(df):
    return df.groupby('customer_state')['price'].sum().reset_index(name='total').sort_values(by='total', ascending=False)

def order_per_city(df):
    return df.groupby('customer_city').size().reset_index(name='total').sort_values(by='total', ascending=False)

def order_per_state(df):
    return df.groupby('customer_state').size().reset_index(name='total').sort_values(by='total', ascending=False)

def product_laris_item(df):
    return df.groupby(by='product_category_name_english').size().reset_index(name='total').sort_values(by='total', ascending=False)

def product_laris(df):
    return df.groupby(by='product_category_name_english')['price'].sum().reset_index(name='total').sort_values(by='total',ascending=False)

def purchased_per_time(df):
    return df.groupby(pd.Grouper(key='order_purchase_timestamp', freq='M')).size().reset_index(name='total').sort_values(by='order_purchase_timestamp')

purchased_per_city_df = purchased_per_city(all_df)
purchased_per_state_df = purchased_per_state(all_df)
order_per_city_df = order_per_city(all_df)
order_per_state_df = order_per_state(all_df)
product_laris_item_df = product_laris_item(all_df)
product_laris_df = product_laris(all_df)
# purchased_per_time_df = purchased_per_time(all_df)

st.header("DASHBOARD PROYEK ANALISIS DATA")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Kota dengan Penjualan Paling banyak")
    fig, ax = plt.subplots(figsize=(6, 6))
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    sns.barplot(
        x='total',
        y='customer_city',
        data=order_per_city_df.sort_values(by='total', ascending=False).head(5),
        palette=colors,
    )
    plt.ylabel(None)
    plt.xlabel(None)
    plt.title("The city with the highest sales", loc='center', fontsize=15)
    plt.tick_params(axis='y', labelsize=12)
    st.pyplot(fig)

with col2:
    st.subheader("Kota dengan Penjualan Paling sedikit")
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    sns.barplot(
        x='total',
        y='customer_city',
        data=order_per_city_df.sort_values(by='total', ascending=True).head(5),
        palette=colors,
    )
    plt.ylabel(None)
    plt.xlabel(None)
    plt.gca().invert_xaxis()
    plt.gca().yaxis.set_label_position('right')
    plt.gca().yaxis.tick_right()
    plt.title("The city with the lowest sales", loc='center', fontsize=15)
    plt.tick_params(axis='y', labelsize=12)

    # Menampilkan plot kedua di Streamlit
    st.pyplot(fig2)

st.subheader(" ")
st.subheader("Performa penjualan di setiap State")
st.subheader(" ")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Kota dengan Penjualan Paling banyak")
    fig, ax = plt.subplots(figsize=(6, 6))
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    sns.barplot(
        x='total',
        y='customer_state',
        data=order_per_state_df.sort_values(by='total', ascending=False).head(5),
        palette=colors,
    )
    plt.ylabel(None)
    plt.xlabel(None)
    plt.title("The state with the highest sales", loc='center', fontsize=15)
    plt.tick_params(axis='y', labelsize=12)
    st.pyplot(fig)

with col2:
    st.subheader("Kota dengan Penjualan Paling sedikit")
    fig2, ax2 = plt.subplots(figsize=(6, 6))
    sns.barplot(
        x='total',
        y='customer_state',
        data=order_per_state_df.sort_values(by='total', ascending=True).head(5),
        palette=colors,
    )
    plt.ylabel(None)
    plt.xlabel(None)
    plt.gca().invert_xaxis()
    plt.gca().yaxis.set_label_position('right')
    plt.gca().yaxis.tick_right()
    plt.title("The state with the lowest sales", loc='center', fontsize=15)
    plt.tick_params(axis='y', labelsize=12)

    # Menampilkan plot kedua di Streamlit
    st.pyplot(fig2)

st.subheader(" ")
st.subheader("Insight Penjualan: Daerah dengan Pengeluaran Tertinggi dan Terendah")
st.subheader(" ")

st.subheader("City")
fig , ax = plt.subplots(nrows=1, ncols=2, figsize=(12,6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x = 'total',
    y = 'customer_city',
    data = purchased_per_city_df.sort_values(by='total', ascending=False).head(5),
    palette=colors,
    ax=ax[0]
)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("The city with the highest purchased", loc='center', fontsize=15)
ax[0].tick_params(axis = 'y', labelsize = 12)

sns.barplot(
    x = 'total',
    y = 'customer_city',
    data = purchased_per_city_df.sort_values(by='total', ascending=True).head(5),
    palette=colors,
    ax=ax[1]
)
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position('right')
ax[1].yaxis.tick_right()
ax[1].set_title("The city with the lowest purchased", loc='center', fontsize=15)
ax[1].tick_params(axis = 'y', labelsize=12)

plt.suptitle("The city with the highest and the lowest purchased", fontsize=20)
plt.show()
st.pyplot(fig)

st.subheader("State")
fig , ax = plt.subplots(nrows=1, ncols=2, figsize=(12,6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x = 'total',
    y = 'customer_state',
    data = purchased_per_state_df.sort_values(by='total', ascending=False).head(5),
    palette=colors,
    ax=ax[0]
)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("The state with the highest purchased", loc='center', fontsize=15)
ax[0].tick_params(axis = 'y', labelsize = 12)

sns.barplot(
    x = 'total',
    y = 'customer_state',
    data = purchased_per_state_df.sort_values(by='total', ascending=True).head(5),
    palette=colors,
    ax=ax[1]
)
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position('right')
ax[1].yaxis.tick_right()
ax[1].set_title("The state with the lowest purchased", loc='center', fontsize=15)
ax[1].tick_params(axis = 'y', labelsize=12)

plt.suptitle("The state with the highest and the lowest purchased", fontsize=20)
plt.show()
st.pyplot(fig)

st.subheader("")
st.subheader("Analisis Penjualan: Produk Paling Laris")
st.subheader("")
fig , ax = plt.subplots(nrows=1, ncols=2, figsize=(12,6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x = 'total',
    y = 'product_category_name_english',
    data = product_laris_item_df.sort_values(by='total', ascending=False).head(5),
    palette=colors,
    ax=ax[0]
)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Produk yang paling banyak terjual", loc='center', fontsize=15)
ax[0].tick_params(axis = 'y', labelsize = 12)

sns.barplot(
    x = 'total',
    y = 'product_category_name_english',
    data = product_laris_item_df.sort_values(by='total', ascending=True).head(5),
    palette=colors,
    ax=ax[1]
)
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position('right')
ax[1].yaxis.tick_right()
ax[1].set_title("Produk yang paling sedikit terjual", loc='center', fontsize=15)
ax[1].tick_params(axis = 'y', labelsize=12)

plt.suptitle("product yang paling banyak dan paling sedikit terjual", fontsize=20)
plt.show()
st.pyplot(fig)

st.subheader("")
st.subheader("Analisis Penjualan: Produk dengan Omset Terkecil dan Terbesar")
st.subheader("")

fig , ax = plt.subplots(nrows=1, ncols=2, figsize=(12,6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(
    x = 'total',
    y = 'product_category_name_english',
    data = product_laris_df.sort_values(by='total', ascending=False).head(5),
    palette=colors,
    ax=ax[0]
)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Produk dengan omset terbesar", loc='center', fontsize=15)
ax[0].tick_params(axis = 'y', labelsize = 12)

sns.barplot(
    x = 'total',
    y = 'product_category_name_english',
    data = product_laris_df.sort_values(by='total', ascending=True).head(5),
    palette=colors,
    ax=ax[1]
)
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position('right')
ax[1].yaxis.tick_right()
ax[1].set_title("Produk dengan omset terkecil", loc='center', fontsize=15)
ax[1].tick_params(axis = 'y', labelsize=12)

plt.suptitle("Product dengan omset terkecil dan terbesar", fontsize=20)
plt.show()
st.pyplot(fig)