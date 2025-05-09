import streamlit as st

def calculate_protein_requirement(weight, activity_level):
    # Rekomendasi kebutuhan protein per kg berat badan menurut aktivitas
    # Sedentary: 0.8 g/kg, Moderate: 1.2 g/kg, Active: 1.6 g/kg
    multiplier = {
        'Sedentary (tidak aktif)': 0.8,
        'Moderate (cukup aktif)': 1.2,
        'Active (sangat aktif)': 1.6
    }
    return weight * multiplier[activity_level]

def main():
    st.title('Kalkulator Kebutuhan Protein Harian')

    st.markdown("""
    <style>
    .stApp {
        background-image: radial-gradient(white 10%, transparent 11%), radial-gradient(white 10%, transparent 11%);
        background-color: #ff69b4;
        background-position: 0 0, 25px 25px;
        background-size: 50px 50px;
        font-size: 25px !important;
    }
    h1 {
        font-size: 40px !important;
    }
    h2 {
        font-size: 30px !important;
    }
    </style>
""", unsafe_allow_html=True)


    menu = st.sidebar.selectbox("Menu", ('Tentang Aplikasi', 'Kalkulator', 'Perkenalan Kelompok'))

    if menu == 'Kalkulator':
        st.subheader('Hitung Kebutuhan Protein Harian Anda')

        weight = st.number_input('Masukkan berat badan Anda (dalam kg):', min_value=1.0, step=0.1)
        activity_level = st.selectbox('Pilih tingkat aktivitas Anda:', [
            'Sedentary (tidak aktif)', 
            'Moderate (cukup aktif)', 
            'Active (sangat aktif)'
        ])

        if weight:
            protein_needed = calculate_protein_requirement(weight, activity_level)
            st.success(f"Kebutuhan protein harian Anda adalah sekitar **{protein_needed:.1f} gram** per hari.")

    elif menu == 'Perkenalan Kelompok':
        st.subheader('Kelompok 3 (1E-PMIP)')
        st.write('Anggota:')
        st.write('1. Dhika Nurafliansyah (2320517)')
        st.write('2. Herni Khairunisa (2320528)')
        st.write('3. Ibnu Rafif (2320530)')
        st.write('4. Khaira Mutya Arrahman (2320533)')
        st.write('5. Marsya Kaila Avridita Mulyono (2320535)')

    elif menu == 'Tentang Aplikasi':
        st.subheader('Tentang Aplikasi')
        st.markdown('<style>.my-gif { width: 500px; height: auto; }</style>', unsafe_allow_html=True)
        st.markdown('<img src="https://jonmgomes.com/wp-content/uploads/2020/05/Comp_1.gif" class="my-gif">', unsafe_allow_html=True)
        st.write(' ')
        st.write('Aplikasi ini membantu pengguna menghitung kebutuhan protein harian berdasarkan berat badan dan tingkat aktivitas. Cocok digunakan oleh pelajar, atlet, atau siapa saja yang ingin menjaga asupan nutrisi optimal.')

if __name__ == '__main__':
    main()
