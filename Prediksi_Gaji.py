import streamlit as st      # membuat aplikasi berjalan di browser
import joblib               # membaca model
import numpy as np

# Memuat model regresi linier yang sudah disimpan
lin_reg_loaded = joblib.load('prediksi_gaji.joblib')

# Judul aplikasi
st.title("Prediksi Gaji Berdasarkan Lama Bekerja")

# Input tahun pengalaman kerja
years_experience = st.number_input(
    "Masukkan jumlah tahun bekerja:",
    min_value=0.0,
    step=0.1
)

# Tombol prediksi
if st.button("Prediksi Gaji"):
    # Data harus berbentuk array 2D
    gaji = lin_reg_loaded.predict([[years_experience]])
    gaji = gaji*17000
    st.write(
        f"Gaji seseorang setelah bekerja selama {years_experience} tahun adalah "
        f"Rp.{gaji[0]:,.2f}"
    )
