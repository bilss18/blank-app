import streamlit as st
import base64

# Set page config
st.set_page_config(page_title="Kalkulator Protein", layout="centered")

# CSS: background navy, teks putih, motif dari gambar yang kamu upload
def set_custom_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    body {{
        background-color: #001f3f;
        color: white;
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Fungsi autoplay audio
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

# Fungsi tampilkan gambar gif
def show_gif(file_path: str, width=300):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <img src="data:image/gif;base64,{b64}" width="{width}">
        """
        st.markdown(md, unsafe_allow_html=True)

# Terapkan background
set_custom_background("gambar protein.jpg")

# Tampilkan gif avocado dan patrick
col1, col2 = st.columns(2)
with col1:
    show_gif("avocado.gif", width=250)
with col2:
    show_gif("patrick.gif", width=250)

# Autoplay audio (jika ada file)
# autoplay_audio("your_audio.mp3")  # Uncomment ini kalau kamu sudah punya file audio

# Judul
st.markdown("<h1 style='text-align: center;'>Kalkulator Protein Harian</h1>", unsafe_allow_html=True)

# Form input pengguna
with st.form("protein_form"):
    berat = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0)
    tujuan = st.selectbox("Pilih tujuan Anda:", [
        "Menambah berat badan ringan",
        "Menambah berat badan sedang",
        "Menambah berat badan cepat",
        "Menambah berat badan sangat cepat"
    ])
    submitted = st.form_submit_button("Hitung")

    if submitted:
        faktor = {
            "Menambah berat badan ringan": 1.4,
            "Menambah berat badan sedang": 1.6,
            "Menambah berat badan cepat": 1.8,
            "Menambah berat badan sangat cepat": 2.0
        }
        kebutuhan = berat * faktor[tujuan]
        st.markdown(f"<h2>Kebutuhan protein Anda: {kebutuhan:.1f} gram/hari</h2>", unsafe_allow_html=True)
