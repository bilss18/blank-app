import streamlit as st

def calculate_protein_requirement(weight, activity_level, gender, age):
    # Rekomendasi dasar
    multiplier = {
        'Sedentary (tidak aktif)': 0.8,
        'Moderate (cukup aktif)': 1.2,
        'Active (sangat aktif)': 1.6
    }

    # Penyesuaian tambahan berdasarkan jenis kelamin dan usia
    adjustment = 0
    if gender == 'Perempuan' and age >= 60:
        adjustment = -0.1
    elif gender == 'Laki-laki' and age >= 60:
        adjustment = 0.1

    return weight * (multiplier[activity_level] + adjustment)

def show_food_recommendations():
    st.markdown("🍽️ **Rekomendasi Makanan Tinggi Protein:**")
    st.markdown("- 🥩 Daging ayam tanpa kulit")
    st.markdown("- 🐟 Ikan salmon atau tuna")
    st.markdown("- 🥚 Telur rebus")
    st.markdown("- 🧀 Tahu / Tempe")
    st.markdown("- 🥛 Susu rendah lemak atau greek yogurt")
    st.markdown("- 🥜 Kacang almond atau edamame")

def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")

    # Gaya latar belakang langit dan awan
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Comic+Neue&display=swap');
        .stApp {
            background: linear-gradient(to bottom, #87CEFA, #ffffff);
            background-image:
                radial-gradient(white 15%, transparent 16%),
                radial-gradient(white 15%, transparent 16%);
            background-size: 100px 100px;
            background-position: 0 0, 50px 50px;
            font-family: 'Comic Neue', cursive !important;
        }
        h1, h2, h3, .stTextInput>div>div>input, .stSelectbox>div>div>div {
            font-family: 'Comic Neue', cursive !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title('😸 Kalkulator Kebutuhan Protein Harian 🥚')

    menu = st.sidebar.selectbox("📋 Menu", ('Tentang Aplikasi', 'Kalkulator', 'Perkenalan Kelompok'))

    if menu == 'Kalkulator':
        st.subheader('✨ Hitung Protein Harian Anda di sini!')

        age = st.number_input('📅 Masukkan umur Anda (tahun):', min_value=1, step=1)
        gender = st.selectbox('🚻 Pilih jenis kelamin Anda:', ['Laki-laki', 'Perempuan'])
        weight = st.number_input('⚖️ Masukkan berat badan Anda (kg):', min_value=1.0, step=0.1)
        activity_level = st.selectbox('🏃‍♀️ Pilih tingkat aktivitas Anda:', [
            'Sedentary (tidak aktif)', 
            'Moderate (cukup aktif)', 
            'Active (sangat aktif)'
        ])

        if weight and age:
            protein_needed = calculate_protein_requirement(weight, activity_level, gender, age)
            st.success(f"🍳 Kebutuhan protein harian Anda adalah sekitar **{protein_needed:.1f} gram** per hari 😋.")

            show_food_recommendations()

    elif menu == 'Perkenalan Kelompok':
        st.subheader('👩‍🏫 Kelompok 5 (1E-PMIP)')
        st.write('📚 Anggota:')
        st.write('1. Chelsea Naila Darmayanti (2420581) 🧠')
        st.write('2. Fadliansyah (2420599) ✨')
        st.write('3. Nabila Kirania (2420629) 🚀')
        st.write('4. Sopian Darul Kamal (2420666) 🌼')
        st.write('5. Suci Rahmawati Sahfitri (2420668) 🎀')

    elif menu == 'Tentang Aplikasi':
        st.subheader('🌈 Tentang Aplikasi')
        st.markdown('<style>.my-gif { width: 500px; height: auto; }</style>', unsafe_allow_html=True)
        st.markdown('<img src="https://jonmgomes.com/wp-content/uploads/2020/05/Comp_1.gif" class="my-gif">', unsafe_allow_html=True)
        st.write(" ")
        st.write("Aplikasi ini membantu pengguna menghitung kebutuhan protein harian berdasarkan berat badan, usia, jenis kelamin, dan aktivitas. Cocok digunakan untuk siapa saja yang ingin menjaga pola makan sehat 💪🍱.")

if __name__ == '__main__':
    main()
