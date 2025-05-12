import streamlit as st

# Fungsi untuk menghitung kebutuhan protein
def calculate_protein_requirement(weight, activity_level, gender, age, goal):
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
        'Meningkatkan massa otot': 0.2
    }

    dasar = weight * (multiplier[activity_level] + gender_age_adj)
    tambahan = weight * goal_adj[goal]
    total = dasar + tambahan

    return total, dasar, tambahan

# Fungsi rekomendasi makanan
def show_food_recommendations():
    st.markdown("🍽 **Rekomendasi Makanan Tinggi Protein:**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- 🥩 Daging ayam tanpa kulit")
        st.markdown("- 🐟 Ikan salmon atau tuna")
        st.markdown("- 🥚 Telur rebus")
    with col2:
        st.markdown("- 🧀 Tahu / Tempe")
        st.markdown("- 🥛 Susu rendah lemak / greek yogurt")
        st.markdown("- 🥜 Kacang almond / edamame")

# Fungsi utama aplikasi
def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")

    # Gaya latar belakang lilac
    st.markdown("""
        <style>
        .stApp {
            background-color: #E6CCF5;
            font-family: 'Comic Sans MS', cursive;
        }
        html, body, [class*="css"] {
            color: #000000;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title('🍳 Kalkulator Kebutuhan Protein Harian 😸')

    # Menu samping
    menu = st.sidebar.selectbox("📋 Menu", ('Tentang Aplikasi', 'Kalkulator', 'Perkenalan Kelompok'))

    if menu == 'Kalkulator':
        st.subheader('✨ Hitung Protein Harian Anda di sini!')

        # Input data pengguna
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
            'Meningkatkan massa otot'
        ])

        if st.button("✅ OK, Hitung Kebutuhan Protein"):
            total, dasar, tambahan = calculate_protein_requirement(weight, activity_level, gender, age, goal)

            # Menampilkan hasil perhitungan
            with st.expander("📊 Lihat Hasil Perhitungan Kebutuhan Protein Anda"):
                st.success(f"🍗 Kebutuhan protein harian Anda untuk *{goal.lower()}* adalah sekitar *{total:.1f} gram* per hari! 😋")
                st.markdown(f"""
                    <ul>
                    <li>Berat badan: {weight} kg</li>
                    <li>Tinggi badan: {height} cm</li>
                    <li>Kebutuhan dasar: {dasar:.1f} gram</li>
                    <li>Penyesuaian karena tujuan: {tambahan:+.1f} gram</li>
                    </ul>
                """, unsafe_allow_html=True)

                # Gambar alpukat lucu
                st.image("avocado.webp", width=300)

                # Suara lucu
                st.audio("cartoon-sfx-cheerful-wow-wah-cute-adorable-surprised-338343.mp3")

                show_food_recommendations()

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
        st.write("Aplikasi ini membantu pengguna menghitung kebutuhan protein harian berdasarkan berat badan, tinggi badan, usia, jenis kelamin, tingkat aktivitas, dan tujuan. Cocok digunakan oleh siapa saja yang ingin menjaga pola makan sehat 💪🍱.")

# Jalankan aplikasi
if __name__ == '__main__':
    main()
