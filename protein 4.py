import streamlit as st
import base64

# Fungsi untuk encode audio dan tampilkan autoplay
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

# Penambahan data makanan lokal (protein per porsi dan deskripsi)
local_foods = [
    {"name": "Tempe", "desc": "Fermentasi kedelai, sumber protein nabati tinggi", "protein": 19},
    {"name": "Tahu", "desc": "Produk kedelai yang lembut, mudah diolah", "protein": 8},
    {"name": "Ayam kampung tanpa kulit", "desc": "Daging ayam dengan protein tinggi dan rendah lemak", "protein": 27},
    {"name": "Ikan bandeng", "desc": "Ikan air tawar kaya protein dan omega-3", "protein": 22},
    {"name": "Telur ayam", "desc": "Sumber protein lengkap dengan asam amino esensial", "protein": 13},
    {"name": "Kacang tanah", "desc": "Sumber protein nabati dan lemak sehat", "protein": 26},
    {"name": "Udang", "desc": "Protein hewani rendah lemak dan kolesterol", "protein": 20},
]

# Fungsi perhitungan protein dengan tambahan kondisi medis
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
        'Meningkatkan massa otot': 0.2
    }

    medical_adj = 0
    if medical_condition == 'Hamil':
        medical_adj = 0.3  # Tambah 30%
    elif medical_condition == 'Penyakit ginjal':
        medical_adj = -0.2  # Kurangi 20%
    elif medical_condition == 'Penyakit hati':
        medical_adj = -0.15  # Kurangi 15%

    dasar = weight * (multiplier[activity_level] + gender_age_adj)
    tambahan = weight * goal_adj[goal]
    medical = weight * medical_adj
    total = dasar + tambahan + medical

    return total, dasar, tambahan, medical

# Fungsi rekomendasi makanan lokal
def show_food_recommendations():
    st.markdown("🍽 *Rekomendasi Makanan Lokal Tinggi Protein:*")
    for food in local_foods:
        st.markdown(f"- **{food['name']}**: {food['desc']} — *Protein: {food['protein']} gram per porsi*")

# Fungsi simulasi piring protein
def show_protein_plate_simulation(total_protein):
    st.markdown("### 🍽️ Simulasi Piring Protein Anda")
    target_per_portion = total_protein / 3
    st.write(f"Kebutuhan protein total: **{total_protein:.1f} gram**")
    st.markdown("Piring dibagi menjadi 3 bagian porsi protein lokal:")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"🥚 **Telur ayam**\n- {target_per_portion:.1f} gram protein")
    with col2:
        st.markdown(f"🍗 **Ayam kampung tanpa kulit**\n- {target_per_portion:.1f} gram protein")
    with col3:
        st.markdown(f"🍲 **Tempe**\n- {target_per_portion:.1f} gram protein")

# Main function
def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")

    # CSS disederhanakan untuk warna font hitam & styling dasar + tombol oranye
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
        div.stButton > button:first-child {
            background-color: orange;
            color: white;
            font-weight: bold;
            height: 40px;
            border-radius: 10px;
            border: none;
        }
        div.stButton > button:first-child:hover {
            background-color: darkorange;
            color: white;
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
            'Meningkatkan massa otot'
        ])
        medical_condition = st.selectbox('🩺 Kondisi Medis:', [
            'Normal', 'Hamil', 'Penyakit ginjal', 'Penyakit hati'
        ])

        if st.button("✅ OK, Hitung Kebutuhan Protein"):
            total, dasar, tambahan, medical = calculate_protein_requirement(weight, activity_level, gender, age, goal, medical_condition)

            with st.expander("📊 Lihat Hasil Perhitungan Kebutuhan Protein Anda"):
                st.success(f"🍗 Kebutuhan protein harian Anda untuk {goal.lower()} dengan kondisi {medical_condition.lower()} adalah sekitar {total:.1f} gram per hari! 😋")
                st.markdown(f"""
                    <ul>
                    <li>Berat badan: {weight} kg</li>
                    <li>Tinggi badan: {height} cm</li>
                    <li>Kebutuhan dasar: {dasar:.1f} gram</li>
                    <li>Penyesuaian karena tujuan: {tambahan:+.1f} gram</li>
                    <li>Penyesuaian kondisi medis: {medical:+.1f} gram</li>
                    </ul>
                """, unsafe_allow_html=True)

                show_avocado_image("avocado.webp")
                autoplay_audio("snd_fragment_retrievewav-14728.mp3")
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
        st.image("foto patrik.gif", caption="Patrick makan demi protein!", use_container_width=True)
        st.write("Aplikasi ini membantu pengguna menghitung kebutuhan protein harian berdasarkan berat badan, tinggi badan, usia, jenis kelamin, tingkat aktivitas, tujuan, dan kondisi medis. Cocok digunakan oleh siapa saja yang ingin menjaga pola makan sehat 💪🍱.")

if __name__ == '__main__':
    main()
