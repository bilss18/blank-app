import streamlit as st
import base64

# Encode gambar background dari file lokal
def get_base64_bg_image(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        return base64.b64encode(data).decode()

# Fungsi untuk menampilkan audio autoplay
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

# Kalkulasi kebutuhan protein
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
        'Mengurangi berat badan': -0.1,
        'Mempertahankan berat badan': 0,
        'Menambah berat badan': 0.2,
        'Menaikkan massa otot': 0.4
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

# Rekomendasi makanan
def show_food_recommendations():
    st.markdown("🍽 *Rekomendasi Makanan Lokal Tinggi Protein:*")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- 🐓 Ayam kampung — 27g/100g")
        st.markdown("- 🐟 Bandeng — 19g/100g")
        st.markdown("- 🥚 Telur ayam kampung — 13g/butir")
    with col2:
        st.markdown("- 🧀 Tahu — 8g/100g")
        st.markdown("- 🌱 Tempe — 19g/100g")
        st.markdown("- 🌰 Kacang tanah — 26g/100g")

# Simulasi piring
def show_protein_plate():
    st.markdown("🍽 **Simulasi Piring Protein Anda**")
    st.markdown("""
    - 1/3: Ayam panggang  
    - 1/3: Tempe + Tahu  
    - 1/3: Sayuran hijau  
    """)

# Fungsi utama
def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")

    # Ambil gambar latar belakang (dari file "gambar protein.jpg")
    b64_image = get_base64_bg_image("gambar protein.jpg")

    # CSS: background + style tombol oranye
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{b64_image}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            color: white;
        }}
        .stMarkdown, .stTextInput, .stSelectbox, label {{
            color: white !important;
        }}
        h1, h2, h3, h4, h5, h6, p {{
            color: white !important;
        }}
        .css-1offfwp {{
            background-color: rgba(0, 0, 0, 0.5) !important;
        }}
        section[data-testid="stSidebar"] .stSelectbox > div {{
            background-color: black !important;
            color: white !important;
            border-radius: 8px;
        }}
        section[data-testid="stSidebar"] label[for^="Menu"]::after {{
            content: "Menu";
            font-weight: bold;
            color: white;
            margin-left: 10px;
        }}
        section[data-testid="stSidebar"] .stSelectbox > div::after {{
            display: none !important;
        }}

        /* Tombol oranye */
        div.stButton > button:first-child {{
            background-color: orange;
            color: white;
            border-radius: 8px;
            font-weight: bold;
        }}
        div.stButton > button:first-child:hover {{
            background-color: darkorange;
            color: white;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.title('🍳 Kalkulator Kebutuhan Protein Harian 😸')

    menu = st.sidebar.selectbox("📋 Menu", ('Tentang Aplikasi', 'Kalkulator', 'Perkenalan Kelompok'))

    if menu == 'Kalkulator':
        st.subheader('✨ Hitung Protein Harian Anda di sini!')

        age = st.number_input('📅 Umur (tahun):', min_value=1, step=1)
        gender = st.selectbox('🚻 Jenis Kelamin:', ['Laki-laki', 'Perempuan'])
        height = st.number_input('📏 Tinggi (cm):', min_value=50, step=1)
        weight = st.number_input('⚖ Berat (kg):', min_value=1.0, step=0.1)
        activity_level = st.selectbox('🏃‍♀ Aktivitas:', [
            'Sedentary (tidak aktif)', 
            'Moderate (cukup aktif)', 
            'Active (sangat aktif)'
        ])
        goal = st.selectbox('🎯 Tujuan:', [
            'Mengurangi berat badan', 
            'Mempertahankan berat badan',
            'Menambah berat badan',
            'Menaikkan massa otot'
        ])
        medical_condition = st.selectbox('🩺 Kondisi medis:', [
            'Tidak ada',
            'Hamil',
            'Penyakit ginjal',
            'Diabetes',
            'Lainnya'
        ])

        if st.button("✅ Hitung"):
            total, dasar, tambahan = calculate_protein_requirement(weight, activity_level, gender, age, goal, medical_condition)

            st.success(f"🍗 Kebutuhan protein Anda: {total:.1f} gram/hari untuk tujuan '{goal}'")

            desc_goal = {
                'Mengurangi berat badan': "Mengurangi protein untuk defisit kalori.",
                'Mempertahankan berat badan': "Protein dasar untuk stabilitas tubuh.",
                'Menambah berat badan': "Tambahan besar untuk kenaikan massa.",
                'Menaikkan massa otot': "Tambahan maksimal untuk pembentukan otot."
            }

            st.markdown(f"**Keterangan:** {desc_goal[goal]}")
            st.markdown(f"""
                <ul>
                <li>Berat badan: {weight} kg</li>
                <li>Tinggi badan: {height} cm</li>
                <li>Protein dasar: {dasar:.1f} g</li>
                <li>Penyesuaian: {tambahan:+.1f} g</li>
                </ul>
            """, unsafe_allow_html=True)

            st.image("avocado.webp", width=250)
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
        st.write("Aplikasi ini membantu Anda menghitung kebutuhan protein harian berdasarkan berbagai faktor. Tetap sehat dan semangat makan bergizi!")

if __name__ == '__main__':
    main()
