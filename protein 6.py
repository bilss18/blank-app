import streamlit as st

# Fungsi perhitungan protein dengan kondisi medis dan tujuan lengkap
def calculate_protein_requirement(weight, activity_level, gender, age, goal, medical_condition):
    multiplier = {
        'Sedentary (tidak aktif)': 1.0,
        'Moderate (cukup aktif)': 1.3,
        'Active (sangat aktif)': 1.6
    }

    gender_age_adj = 0
    if gender == 'Perempuan' and age >= 60:
        gender_age_adj = -0.1
    elif gender == 'Laki-laki' and age >= 60:
        gender_age_adj = 0.1

    goal_adj = {
        'Menurunkan berat badan': -0.05,
        'Mempertahankan berat badan': 0,
        'Meningkatkan massa otot': 0.3,
        'Menambah berat badan': 0.25
    }

    medical_adj = {
        'Tidak ada': 0,
        'Hamil (Trimester 1)': 0.1,
        'Hamil (Trimester 2)': 0.2,
        'Hamil (Trimester 3)': 0.25,
        'Penyakit ginjal ringan': -0.15,
        'Diabetes tipe 2': 0.0,
        'Hipertensi': 0.0,
        'Luka pasca operasi': 0.3,
        'Malnutrisi': 0.4
    }

    dasar = weight * (multiplier[activity_level] + gender_age_adj)
    tambahan_goal = weight * goal_adj[goal]
    tambahan_medical = weight * medical_adj[medical_condition]
    total = dasar + tambahan_goal + tambahan_medical

    return total, dasar, tambahan_goal, tambahan_medical

# Rekomendasi makanan lokal dengan keterangan protein
food_list = {
    "Tempe (100g)": (19, "Sumber protein nabati tinggi, murah dan mudah didapat."),
    "Telur rebus (1 butir)": (6, "Protein hewani cepat saji dan padat gizi."),
    "Ikan lele goreng (100g)": (20, "Kaya omega-3 dan protein tinggi."),
    "Dada ayam rebus (100g)": (31, "Protein tinggi, rendah lemak."),
    "Susu kedelai (1 gelas)": (7, "Sumber protein cair nabati."),
    "Tahu putih (100g)": (10, "Serbaguna untuk berbagai masakan.")
}

def show_food_recommendations():
    st.markdown("🍽 **Rekomendasi Makanan Lokal Tinggi Protein:**")
    for name, (protein, note) in food_list.items():
        st.markdown(f"- **{name}**: {protein}g protein — _{note}_")

# Simulasi piring protein dengan makanan lokal
def show_protein_plate_simulation(target_protein):
    st.markdown("🍱 **Simulasi Piring Protein:**")
    options = list(food_list.items())
    selected = []
    remaining = target_protein

    for name, (protein, _) in options:
        if remaining <= 0:
            break
        qty = int(remaining // protein)
        if qty > 0:
            selected.append((qty, name, protein * qty))
            remaining -= protein * qty

    for qty, name, total_protein in selected:
        st.markdown(f"- {qty}x **{name}** → {total_protein:.1f}g protein")

    if remaining > 0:
        st.markdown(f"🔹 Sisa {remaining:.1f}g protein, bisa dilengkapi dengan camilan tinggi protein seperti susu atau kacang.")

# Fungsi autoplay audio tanpa base64, pakai st.audio
def play_audio(file_path):
    audio_file = open(file_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

# Fungsi tampilkan gambar GIF
def show_gif(file_path, caption=None):
    st.image(file_path, caption=caption, use_column_width=True)

# Fungsi utama aplikasi
def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")

    # Styling tombol oranye agar lebih terlihat, tanpa mengubah tampilan lain
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #FFA500;
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
        medical_condition = st.selectbox('🩺 Kondisi Medis (jika ada):', [
            'Tidak ada', 'Hamil (Trimester 1)', 'Hamil (Trimester 2)', 'Hamil (Trimester 3)',
            'Penyakit ginjal ringan', 'Diabetes tipe 2', 'Hipertensi', 'Luka pasca operasi', 'Malnutrisi'
        ])

        if st.button("✅ OK, Hitung Kebutuhan Protein"):
            total, dasar, tambahan_goal, tambahan_medical = calculate_protein_requirement(
                weight, activity_level, gender, age, goal, medical_condition
            )

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

            show_gif("foto patrik.gif", caption="Patrick makan demi protein!")
            play_audio("snd_fragment_retrievewav-14728.mp3")
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
        st.image("foto patrik.gif", caption="Patrick makan demi protein!", use_column_width=True)
        st.write("Aplikasi ini membantu menghitung kebutuhan protein harian berdasarkan berat, tinggi, usia, jenis kelamin, aktivitas, tujuan, dan kondisi medis. Cocok untuk menjaga pola makan sehat 💪🍱.")

if __name__ == '__main__':
    main()
