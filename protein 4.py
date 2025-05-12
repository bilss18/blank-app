import streamlit as st

# Fungsi untuk menghitung kebutuhan protein
def calculate_protein_requirement(weight, activity_level, gender, age):
    multiplier = {
        'Sedentary (tidak aktif)': 0.8,
        'Moderate (cukup aktif)': 1.2,
        'Active (sangat aktif)': 1.6
    }

    adjustment = 0
    if gender == 'Perempuan' and age >= 60:
        adjustment = -0.1
    elif gender == 'Laki-laki' and age >= 60:
        adjustment = 0.1

    return weight * (multiplier[activity_level] + adjustment)

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

    # Gaya latar belakang lilac dan teks hitam
    st.markdown("""
        <style>
        .stApp {
            background-color: #C8A2C8;
            background-size: cover;
            color: #000000;
        }
        html, body, [class*="css"] {
            font-family: 'Comic Sans MS', cursive;
            color: #000000 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title('🍳 Kalkulator Kebutuhan Protein Harian 😸')

    # Menu samping
    menu = st.sidebar.selectbox("📋 Menu", ('Tentang Aplikasi', 'Kalkulator', 'Perkenalan Kelompok'))

    # Kalkulator
    if menu == 'Kalkulator':
        st.subheader('✨ Hitung Protein Harian Anda di sini!')

        # Input data
        age = st.number_input('📅 Masukkan umur Anda (tahun):', min_value=1, step=1)
        gender = st.selectbox('🚻 Pilih jenis kelamin Anda:', ['Laki-laki', 'Perempuan'])
        weight = st.number_input('⚖ Masukkan berat badan Anda (kg):', min_value=1.0, step=0.1)
        activity_level = st.selectbox('🏃‍♀ Pilih tingkat aktivitas Anda:', [
            'Sedentary (tidak aktif)', 
            'Moderate (cukup aktif)', 
            'Active (sangat aktif)'
        ])

        # Tombol OK
        if st.button("✅ OK, Hitung Kebutuhan Protein"):
            protein_needed = calculate_protein_requirement(weight, activity_level, gender, age)
            st.success(f"🍗 Kebutuhan protein harian Anda adalah sekitar *{protein_needed:.1f} gram* per hari! 😋")
            st.markdown('<img src="https://media.tenor.com/1mi8BRdrVjwAAAAC/egg-protein.gif" width="300">', unsafe_allow_html=True)
            show_food_recommendations()

    # Menu Perkenalan
    elif menu == 'Perkenalan Kelompok':
        st.subheader('👩‍🏫 Kelompok 5 (PMIP 1-E1)')
        st.write('📚 Anggota:')
        st.write('1. Chelsea Naila Darmayanti (2420581) 🐣')
        st.write('2. Fadliansyah (2420499) 🐈')
        st.write('3. Nabila Kirania Siti Saleha (2420629) 🦩')
        st.write('4. Sopian Darul Kamal (2420666) 🐿')
        st.write('5. Suci Rahma Safitri (2420668) 🦭')

    # Menu Tentang
    elif menu == 'Tentang Aplikasi':
        st.subheader('🌈 Tentang Aplikasi')
        st.image("foto patrik.gif", caption="Patrick makan demi protein!", use_container_width=True)
        st.write("Aplikasi ini membantu pengguna menghitung kebutuhan protein harian berdasarkan berat badan, usia, jenis kelamin, dan tingkat aktivitas. Cocok digunakan oleh siapa saja yang ingin menjaga pola makan sehat 💪🍱.")

# Jalankan aplikasi
if __name__ == '__main__':
    main()
