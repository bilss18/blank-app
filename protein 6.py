import streamlit as st
import base64

# Fungsi untuk encode dan autoplay audio
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

# Fungsi menampilkan gambar avocado
def show_avocado_image(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <img src="data:image/webp;base64,{b64}" width="300">
        """
        st.markdown(md, unsafe_allow_html=True)

# Fungsi hitung kebutuhan protein harian
def calculate_protein_requirement(weight, activity_level, gender, age, goal, medical_condition):
    multiplier = {
        'Sedentary (tidak aktif)': 0.8,
        'Moderate (cukup aktif)': 1.2,
        'Active (sangat aktif)': 1.6
    }

    gender_age_adj = 0
    if gender == 'Perempuan' and age >= 60:
        gender_age_adj = -0.1
    elif gender == 'Laki-laki' and age >= 60:
        gender_age_adj = 0.1

    goal_adj = {
        'Menurunkan berat badan': -0.1,
        'Mempertahankan berat badan': 0,
        'Menambah berat badan ringan': 0.1,
        'Menambah berat badan sedang': 0.2,
        'Menambah berat badan banyak': 0.3,
        'Menambah berat badan sangat banyak': 0.4
    }

    medical_adj = {
        'Tidak ada': 0,
        'Hamil': 0.5,
        'Penyakit ginjal': -0.3,
        'Diabetes': -0.1,
        'Lainnya': 0
    }

    dasar = weight * (multiplier[activity_level] + gender_age_adj)
    tambahan = weight * goal_adj[goal] + weight * medical_adj[medical_condition]
    total = dasar + tambahan

    return total, dasar, tambahan

# Rekomendasi makanan lokal tinggi protein beserta gram protein perkiraan
def show_food_recommendations():
    st.markdown("🍽 *Rekomendasi Makanan Lokal Tinggi Protein:*")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- 🐓 Ayam kampung tanpa kulit — 27g protein per 100g")
        st.markdown("- 🐟 Ikan bandeng — 19g protein per 100g")
        st.markdown("- 🥚 Telur ayam kampung — 13g protein per butir")
    with col2:
        st.markdown("- 🧀 Tahu — 8g protein per 100g")
        st.markdown("- 🌱 Tempe — 19g protein per 100g")
        st.markdown("- 🌰 Kacang tanah — 26g protein per 100g")

# Simulasi piring protein
def show_protein_plate():
    st.markdown("🍽 **Simulasi Piring Protein Anda**")
    st.markdown("""
    - 1/3 piring: Ayam kampung panggang  
    - 1/3 piring: Tumis tempe dan tahu  
    - 1/3 piring: Sayuran hijau  
    """)

# Fungsi utama aplikasi
def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")

    st.markdown("""
        <style>
        .stApp, html, body {
            background-color: #E6CCF5;
            font-family: 'Comic Sans MS', cursive;
            color: black !important;
        }
        label, .stSidebar, .css-1v3fvcr, .css-1d391kg {
            color: black !important;
        }
        button[kind="primary"] {
            background-color: orange !important;
            color: black !important;
            font-weight: bold !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title('🍳 Kalkulator Kebutuhan Protein Harian 😸')

    menu = st.sidebar.selectbox("📋 Menu", ('Tentang Aplikasi', 'Kalkulator', 'Perkenalan Kelompok'))

    if menu == 'Kalkulator':
        st.subheader('✨ Hitung Protein Harian Anda di sini!')

        age = st.number_input('📅 Masukkan umur Anda (tahun):', min_value=1, step=1)
        gender = st.selectbox('🚻 Pilih jenis kelamin Anda:', ['Laki-laki', 'Perempuan'])
        height = st.number_input('📏 Masukkan tinggi badan Anda (cm):', min_value=50, step=1)
        weight = st.number_input('⚖ Masukkan berat badan Anda (kg):', min_value=1.0, step=0.1)
        activity_level = st.selectbox('🏃‍♀ Pilih tingkat aktivitas Anda:', [
            'Sedentary (tidak aktif)', 
            'Moderate (cukup aktif)', 
            'Active (sangat aktif)'
        ])
        goal = st.selectbox('🎯 Apa tujuan Anda?', [
            'Menurunkan berat badan', 
            'Mempertahankan berat badan',
            'Menambah berat badan ringan',
            'Menambah berat badan sedang',
            'Menambah berat badan banyak',
            'Menambah berat badan sangat banyak'
        ])
        medical_condition = st.selectbox('🩺 Kondisi medis (jika ada):', [
            'Tidak ada',
            'Hamil',
            'Penyakit ginjal',
            'Diabetes',
            'Lainnya'
        ])

        if st.button("✅ OK, Hitung Kebutuhan Protein"):
            total, dasar, tambahan = calculate_protein_requirement(weight, activity_level, gender, age, goal, medical_condition)

            st.success(f"🍗 Kebutuhan protein harian Anda untuk tujuan '{goal}' adalah sekitar {total:.1f} gram per hari! 😋")

            desc_goal = {
                'Menurunkan berat badan': "Pengurangan protein untuk mendukung penurunan berat badan secara sehat.",
                'Mempertahankan berat badan': "Protein dasar untuk menjaga berat badan dan kesehatan otot.",
                'Menambah berat badan ringan': "Penambahan protein ringan untuk meningkatkan berat badan secara bertahap.",
                'Menambah berat badan sedang': "Penambahan protein sedang untuk mendukung peningkatan massa tubuh.",
                'Menambah berat badan banyak': "Penambahan protein signifikan untuk pertumbuhan massa otot dan berat badan.",
                'Menambah berat badan sangat banyak': "Penambahan protein maksimal untuk mempercepat peningkatan berat badan."
            }

            st.markdown(f"**Keterangan:** {desc_goal[goal]}")

            st.markdown(f"""
                <ul>
                <li>Berat badan: {weight} kg</li>
                <li>Tinggi badan: {height} cm</li>
                <li>Kebutuhan dasar: {dasar:.1f} gram</li>
                <li>Penyesuaian karena tujuan & kondisi medis: {tambahan:+.1f} gram</li>
                </ul>
            """, unsafe_allow_html=True)

            show_avocado_image("avocado.webp")
            autoplay_audio("snd_fragment_retrievewav-14728.mp3")

            show_food_recommendations()
            show_protein_plate()

    elif menu == 'Perkenalan Kelompok':
        st.subheader('👩‍🏫 Kelompok 5 (PMIP 1-E1)')
        st.write('📚 Anggota:')
        st.write('1. Chelsea Naila Darmayanti (2420581) 🐣')
        st.write('2. Fadliansyah (2420499) 🐈')
        st.write('3. Nabila Kirania Siti Saleha (2420629) 🦩')
        st.write('4. Sopian Darul Kamal (2420666) 🐿')
        st.write('5. Suci Rahma Safitri (2420668) 🦭')

    elif menu == 'Tentang Aplikasi':
        st.subheader('🌈 Tentang Aplikasi')
        st.image("foto patrik.gif", caption="Patrick makan demi protein!", use_container_width=True)
        st.write("Aplikasi ini membantu pengguna menghitung kebutuhan protein harian berdasarkan berat badan, tinggi badan, usia, jenis kelamin, tingkat aktivitas, tujuan, dan kondisi medis. Cocok digunakan oleh siapa saja yang ingin menjaga pola makan sehat 💪🍱.")

if __name__ == '__main__':
    main()
