# Mengimpor modul yang dibutuhkan
import streamlit as st
import base64

# Fungsi untuk membaca dan mengubah gambar lokal menjadi format base64
def get_base64_bg_image(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        return base64.b64encode(data).decode()

# Fungsi untuk menampilkan audio secara otomatis ketika halaman diakses
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

# Fungsi utama untuk menghitung kebutuhan protein harian berdasarkan berbagai faktor
def calculate_protein_requirement(weight, activity_level, gender, age, goal, medical_condition):
    # Faktor dasar berdasarkan tingkat aktivitas
    multiplier = {
        'Sedentary (tidak aktif)': 0.8,
        'Moderate (cukup aktif)': 1.2,
        'Active (sangat aktif)': 1.6
    }

    # Penyesuaian berdasarkan usia dan jenis kelamin (usia lanjut)
    gender_age_adj = 0
    if gender == 'Perempuan' and age >= 60:
        gender_age_adj = -0.1
    elif gender == 'Laki-laki' and age >= 60:
        gender_age_adj = 0.1

    # Penyesuaian berdasarkan tujuan pengguna
    goal_adj = {
        'Mengurangi berat badan': -0.1,
        'Mempertahankan berat badan': 0,
        'Menambah berat badan': 0.2,
        'Menaikkan massa otot': 0.4
    }

    # Penyesuaian berdasarkan kondisi medis tertentu
    medical_adj = {
        'Tidak ada': 0,
        'Hamil': 0.5,
        'Penyakit ginjal': -0.3,
        'Diabetes': -0.1,
        'Lainnya': 0
    }

    # Perhitungan protein dasar dan tambahan
    dasar = weight * (multiplier[activity_level] + gender_age_adj)
    tambahan = weight * goal_adj[goal] + weight * medical_adj[medical_condition]
    total = dasar + tambahan
    return total, dasar, tambahan

# Menampilkan daftar makanan lokal tinggi protein sebagai rekomendasi
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

# Menampilkan simulasi visual pembagian piring makan tinggi protein
def show_protein_plate():
    st.markdown("🍽 **Simulasi Piring Protein Anda**")
    st.markdown("""
    - 1/3: Ayam panggang  
    - 1/3: Tempe + Tahu  
    - 1/3: Sayuran hijau  
    """)

# Fungsi utama aplikasi
def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")

    # Memuat gambar latar belakang dari file lokal
    b64_image = get_base64_bg_image("gambar protein.jpg")

    # Menetapkan gambar sebagai latar belakang halaman aplikasi menggunakan CSS
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
        </style>
    """, unsafe_allow_html=True)

    st.title('🍳 Kalkulator Kebutuhan Protein Harian 😸')

    # Navigasi menu di sidebar
    menu = st.sidebar.selectbox("📋 Menu", ('Tentang Aplikasi', 'Kalkulator', 'Perkenalan Kelompok'))

    # Halaman Kalkulator
    if menu == 'Kalkulator':
        st.subheader('✨ Hitung Protein Harian Anda di sini!')

        # Form input data pengguna
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

        # Tombol untuk menghitung kebutuhan protein
        if st.button("✅ Hitung"):
            total, dasar, tambahan = calculate_protein_requirement(weight, activity_level, gender, age, goal, medical_condition)

            st.success(f"🍗 Kebutuhan protein Anda: {total:.1f} gram/hari untuk tujuan '{goal}'")

            # Penjelasan hasil berdasarkan tujuan
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

    # Halaman perkenalan kelompok
    elif menu == 'Perkenalan Kelompok':
        st.subheader('👩‍🏫 Kelompok 5 (PMIP 1-E1)')
        st.write('📚 Anggota:')
        st.write('1. Chelsea Naila Darmayanti (2420581) 🐣')
        st.write('2. Fadliansyah (2420499) 🐈')
        st.write('3. Nabila Kirania Siti Saleha (2420629) 🦩')
        st.write('4. Sopian Darul Kamal (2420666) 🐿')
        st.write('5. Suci Rahma Safitri (2420668) 🦭')
        st.image("foto patrik.gif", caption="Patrick makan demi protein!", use_container_width=True)

    # Halaman informasi tentang aplikasi
    elif menu == 'Tentang Aplikasi':
        st.subheader('🌈 Tentang Aplikasi')
        st.image("foto patrik.gif", caption="Patrick makan demi protein!", use_container_width=True)
        st.write("Aplikasi ini membantu pengguna menghitung kebutuhan protein harian berdasarkan berat badan, tinggi badan, usia, jenis kelamin, tingkat aktivitas, tujuan, dan kondisi medis. Cocok digunakan oleh siapa saja yang ingin menjaga pola makan sehat 💪🍱.")

# Menjalankan aplikasi
if __name__ == '__main__':
    main()
