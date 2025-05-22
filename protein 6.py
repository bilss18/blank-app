import streamlit as st

# Fungsi perhitungan protein
def calculate_protein_requirement(weight, activity_level, gender, age, goal, medical_condition):
    # Multiplier aktivitas
    multiplier = {
        'Sedentary (tidak aktif)': 0.8,
        'Moderate (cukup aktif)': 1.2,
        'Active (sangat aktif)': 1.6
    }

    # Penyesuaian gender dan usia
    gender_age_adj = 0
    if gender == 'Perempuan' and age >= 60:
        gender_age_adj = -0.1
    elif gender == 'Laki-laki' and age >= 60:
        gender_age_adj = 0.1

    # Penyesuaian tujuan
    goal_adj = {
        'Menurunkan berat badan': -0.1,
        'Mempertahankan berat badan': 0,
        'Meningkatkan massa otot': 0.2,
        'Menambah berat badan': 0.15
    }

    # Penyesuaian kondisi medis
    medical_adj = {
        'Normal': 0,
        'Hamil': 0.3,
        'Penyakit Ginjal': -0.3
    }

    dasar = weight * (multiplier[activity_level] + gender_age_adj)
    tambahan_goal = weight * goal_adj[goal]
    tambahan_medical = weight * medical_adj[medical_condition]
    total = dasar + tambahan_goal + tambahan_medical

    return total, dasar, tambahan_goal, tambahan_medical

# Keterangan tujuan
def goal_description(goal):
    desc = {
        'Menurunkan berat badan': 'Protein sedikit dikurangi karena kebutuhan energi berkurang saat menurunkan berat badan.',
        'Mempertahankan berat badan': 'Protein dipertahankan sesuai kebutuhan dasar tubuh untuk menjaga massa otot.',
        'Meningkatkan massa otot': 'Protein ditingkatkan untuk mendukung pembentukan dan pemulihan otot.',
        'Menambah berat badan': 'Protein ditambah untuk membantu pertumbuhan massa otot dan jaringan tubuh.'
    }
    return desc.get(goal, "")

# Rekomendasi makanan lokal tinggi protein (dengan keterangan gram protein per 100 gram)
def show_food_recommendations():
    st.markdown("### 🍽 Rekomendasi Makanan Lokal Tinggi Protein")
    makanan = {
        "Tempe": 19,
        "Tahu": 8,
        "Telur Ayam": 13,
        "Ikan Bandeng": 18,
        "Ayam Kampung (dada)": 23,
        "Udang": 20,
        "Kacang Hijau": 24,
    }
    for makanan_nama, protein_gram in makanan.items():
        st.write(f"- {makanan_nama}: {protein_gram} gram protein per 100 gram")

# Simulasi piring protein sederhana
def show_protein_plate_simulation(protein_need):
    st.markdown("### 🍽 Simulasi Piring Protein Harian Anda")
    st.write(f"Anda membutuhkan sekitar **{protein_need:.1f} gram** protein per hari.")

    # Asumsi 3 porsi protein, bagi rata
    porsi = protein_need / 3
    st.write("Misalnya, Anda bisa membagi kebutuhan protein ke dalam 3 porsi makanan utama:")

    st.write(f"- Porsi 1: ~{porsi:.1f} gram protein")
    st.write(f"- Porsi 2: ~{porsi:.1f} gram protein")
    st.write(f"- Porsi 3: ~{porsi:.1f} gram protein")

    st.info("Contoh kombinasi porsi dari makanan lokal bisa seperti: Tempe + Telur + Ayam Kampung")

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
        /* Tombol warna oranye */
        div.stButton > button:first-child {
            background-color: orange;
            color: black;
            font-weight: bold;
            height: 3em;
            font-size: 18px;
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
            'Meningkatkan massa otot', 
            'Menambah berat badan'
        ])
        medical_condition = st.selectbox('⚕ Kondisi medis (jika ada):', [
            'Normal',
            'Hamil',
            'Penyakit Ginjal'
        ])

        if st.button("✅ OK, Hitung Kebutuhan Protein"):
            total, dasar, tambahan_goal, tambahan_medical = calculate_protein_requirement(
                weight, activity_level, gender, age, goal, medical_condition)

            st.success(f"🍗 Kebutuhan protein harian Anda untuk *{goal.lower()}* adalah sekitar *{total:.1f} gram* per hari! 😋")
            st.markdown(f"""
                <ul>
                <li>Berat badan: {weight} kg</li>
                <li>Tinggi badan: {height} cm</li>
                <li>Kebutuhan dasar: {dasar:.1f} gram</li>
                <li>Penyesuaian karena tujuan: {tambahan_goal:+.1f} gram</li>
                <li>Penyesuaian kondisi medis: {tambahan_medical:+.1f} gram</li>
                </ul>
            """, unsafe_allow_html=True)

            desc = goal_description(goal)
            if desc:
                st.info(f"ℹ️ Keterangan: {desc}")

            show_food_recommendations()
            show_protein_plate_simulation(total)

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
        st.write("Aplikasi ini membantu pengguna menghitung kebutuhan protein harian berdasarkan berat badan, tinggi badan, usia, jenis kelamin, tingkat aktivitas, tujuan, dan kondisi medis. Cocok digunakan oleh siapa saja yang ingin menjaga pola makan sehat 💪🍱.")

if __name__ == '__main__':
    main()
