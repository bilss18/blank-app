import streamlit as st

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

def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")

    # Gunakan background secara langsung menggunakan CSS
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to bottom, #FFD194, #FFCC70);  /* Latar belakang Gradien */
            background-image: url('https://www.transparenttextures.com/patterns/cloudy.png');
            background-size: cover; /* Pastikan pola tekstur menutupi seluruh layar */
            height: 100vh; /* Menjaga latar belakang menutupi seluruh layar */
        }
        .css-ffhzg2 {  /* Selector untuk elemen halaman Streamlit */
            font-family: 'Comic Sans MS', cursive;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title('🍳 Kalkulator Kebutuhan Protein Harian 😸')

    menu = st.sidebar.selectbox("📋 Menu", ('Tentang Aplikasi', 'Kalkulator', 'Perkenalan Kelompok'))

    if menu == 'Kalkulator':
        st.subheader('✨ Hitung Protein Harian Anda di sini!')

        age = st.number_input('📅 Masukkan umur Anda (tahun):', min_value=1, step=1)
        gender = st.selectbox('🚻 Pilih jenis kelamin Anda:', ['Laki-laki', 'Perempuan'])
        weight = st.number_input('⚖ Masukkan berat badan Anda (kg):', min_value=1.0, step=0.1)
        activity_level = st.selectbox('🏃‍♀ Pilih tingkat aktivitas Anda:', [
            'Sedentary (tidak aktif)', 
            'Moderate (cukup aktif)', 
            'Active (sangat aktif)'
        ])

        if weight and age:
            protein_needed = calculate_protein_requirement(weight, activity_level, gender, age)
            st.success(f"🍗 Kebutuhan protein harian Anda adalah sekitar *{protein_needed:.1f} gram* per hari! 😋")
            st.markdown('<img src="https://media.tenor.com/1mi8BRdrVjwAAAAC/egg-protein.gif" width="300">', unsafe_allow_html=True)
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
        st.write("Aplikasi ini membantu pengguna menghitung kebutuhan protein harian berdasarkan berat badan, usia, jenis kelamin, dan tingkat aktivitas. Cocok digunakan oleh siapa saja yang ingin menjaga pola makan sehat 💪🍱.")

if __name__ == '__main__':
    main()
