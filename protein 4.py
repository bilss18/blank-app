import streamlit as st

# Fungsi perhitungan protein
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

    # Penyesuaian berdasarkan tujuan
    goal_adj = {
        'Menurunkan berat badan': -0.1,
        'Mempertahankan berat badan': 0,
        'Meningkatkan massa otot': 0.2,
        'Menambah berat badan': 0.3
    }[goal]

    # Penyesuaian berdasarkan kondisi medis
    condition_adj = 0
    if 'Hamil' in medical_condition:
        condition_adj += 0.3
    if 'Penyakit ginjal ringan' in medical_condition:
        condition_adj -= 0.2
    if 'Penyakit liver' in medical_condition:
        condition_adj -= 0.2

    dasar = weight * (multiplier[activity_level] + gender_age_adj)
    tambahan = weight * (goal_adj + condition_adj)
    total = dasar + tambahan

    return total, dasar, tambahan

# Rekomendasi makanan lokal
def show_food_recommendations():
    st.markdown("🍽 *Rekomendasi Makanan Tinggi Protein Lokal:*")
    st.markdown("""
    - 🍗 Ayam kampung rebus (30g protein per 100g)
    - 🐟 Ikan lele goreng (26g protein per 100g)
    - 🥚 Telur ayam negeri (6g protein per butir)
    - 🧀 Tempe goreng (13g protein per 100g)
    - 🥜 Kacang tanah sangrai (25g protein per 100g)
    - 🥛 Susu kedelai (7g protein per gelas)
    """)

# Simulasi piring protein lokal
def show_protein_plate():
    st.markdown("🍽️ **Simulasi Piring Protein Lokal:**")
    st.markdown("""
    **Contoh Menu:**
    - 100g tempe (13g protein)
    - 1 butir telur rebus (6g protein)
    - 100g ayam rebus (30g protein)
    - 1 gelas susu kedelai (7g protein)

    **Total: ~56g protein**
    """)

# Fungsi utama
def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")

    # CSS dan gaya dari versi awal
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
        .orange-button button {
            background-color: orange;
            color: white;
            font-weight: bold;
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

        medical_condition = st.multiselect('🩺 Kondisi Medis (pilih jika ada):', [
            'Hamil',
            'Penyakit ginjal ringan',
            'Penyakit liver'
        ])

        if st.markdown('<div class="orange-button">', unsafe_allow_html=True) or True:
            if st.button("✅ OK, Hitung Kebutuhan Protein"):
                total, dasar, tambahan = calculate_protein_requirement(
                    weight, activity_level, gender, age, goal, medical_condition
                )

                st.success(f"🍗 Kebutuhan protein harian Anda untuk {goal.lower()} adalah sekitar {total:.1f} gram per hari! 😋")
                st.markdown(f"""
                    <ul>
                    <li>Berat badan: {weight} kg</li>
                    <li>Tinggi badan: {height} cm</li>
                    <li>Kebutuhan dasar: {dasar:.1f} gram</li>
                    <li>Penyesuaian tambahan: {tambahan:+.1f} gram</li>
                    </ul>
                """, unsafe_allow_html=True)

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
