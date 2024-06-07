import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Streamlit başlangıcı
st.title("Takipçi Analizi Dashboard")

# Tek dosya yükleme
uploaded_file = st.file_uploader("Veri setini yükleyin", type=["xls"])

# Grafik türü seçimi
grafik_turu = st.selectbox("Lütfen bir grafik türü seçin:", ["Pasta Grafik", "Çizgi Grafik", "Bar Grafik"])

# Veri setini yükleme ve dönüştürme
def load_and_check_file(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file, engine='xlrd')
        st.write("Yüklenen dosyanın sütunları:", df.columns.tolist())

        if 'Tarih' in df.columns:
            df['Tarih'] = pd.to_datetime(df['Tarih'])
        else:
            st.error("'Tarih' sütunu bulunamadı. Lütfen sütun adlarını kontrol edin.")

        return df
    return None

df = load_and_check_file(uploaded_file)

# Grafik Fonksiyonları
def plot_time_series(data, x, y, title):
    plt.figure(figsize=(10, 5))
    plt.plot(data[x], data[y], marker='o')
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(plt)

def plot_bar_chart(data, category, value, title):
    if category in data.columns and value in data.columns:
        cat_total = data.groupby(category)[value].sum().reset_index()
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(cat_total[category], cat_total[value])
        plt.title(title)
        plt.xlabel(category)
        plt.ylabel(value)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.error(f"'{category}' veya '{value}' sütunları bulunamadı.")

# Dosya yükleme ve işleme
if df is not None:
    st.header("Veri Seti")
    st.write(df.head())

    if grafik_turu == "Çizgi Grafik":
        st.subheader("Çizgi Grafik")
        for column in df.columns:
            if column != 'Tarih':
                plot_time_series(df, 'Tarih', column, f"Tarih vs {column}")
    elif grafik_turu == "Bar Grafik":
        st.subheader("Bar Grafik")
        for column in df.columns:
            if column != 'Tarih':
                plot_bar_chart(df, 'Tarih', column, f"Tarih vs {column}")
    elif grafik_turu == "Pasta Grafik":
        st.subheader("Pasta Grafik")
        for column in df.columns:
            if column != 'Tarih':
                st.write(f"{column} Dağılımı")
                df[column].plot(kind='pie', autopct='%1.1f%%')
                st.pyplot()
