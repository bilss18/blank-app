import streamlit as st
import base64
import matplotlib.pyplot as plt
import pandas as pd

# Fungsi encode dan autoplay audio
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

# Fungsi tampilkan gambar avocado
def show_avocado_image(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <img src="data:image/webp;base64,{b64}" width="300">
        """
        st.markdown(md, unsafe_allow_html=True)

# Hitung kebutuhan protein harian
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

# Data makanan lokal dengan info gizi: (protein, kalori, lemak, karbohidrat, keterangan)
food_list = {
    "Tempe (100g)": (19, 192, 11, 7, "Sumber protein nabati tinggi, murah dan mudah didapat."),
    "Telur rebus (1 butir)": (6, 78, 5, 1, "Protein hewani cepat saji dan padat gizi."),
    "Ikan lele goreng (100g)": (20, 180, 10, 0, "Kaya omega-3 dan protein tinggi."),
    "Dada ayam rebus (100g)": (31, 165, 3.6, 0, "Protein tinggi, rendah lemak."),
    "Susu kedelai (1 gelas)": (7, 100, 4, 8, "Sumber protein cair nabati."),
    "Tahu putih (100g)": (10, 76, 4.8, 1.9, "Serbaguna untuk berbagai masakan.")
}

def show_food_recommendations():
    st.markdown("🍽 **Rekomendasi Makanan Lokal Tinggi Protein:**")
    for name, (protein, kalori, lemak, karbo, note) in food_list.items():
        st.markdown(f"""
        - **{name}**: {protein}g protein  
          📝 _{note}_  
          📊 Kalori: {kalori} kcal, Lemak: {lemak}g, Karbohidrat: {karbo}g
        """)

# Simulasi piring protein lengkap kalori
def show_protein_plate_simulation(target_protein):
    st.markdown("🍱 **Simulasi Piring Protein:**")
    selected = []
    remaining = target_protein
    total_kalori = 0

    for name, (protein, kalori, _, _, _) in food_list.items():
        if remaining <= 0:
            break
        qty = int(remaining // protein)
        if qty > 0:
            total_protein = qty * protein
            total_kal = qty * kalori
            selected.append((qty, name, total_protein, total_kal))
            total_kalori += total_kal
            remaining -= total_protein

    for qty, name, total_protein, total_kal in selected:
        st.markdown(f"- {qty}x **{name}** → {total_protein:.1f}g protein, {total_kal} kcal")

    if remaining > 0:
        st.markdown(f"🔹 Sisa {remaining:.1f}g protein, bisa dilengkapi dengan camilan tinggi protein seperti susu atau kacang.")

    st.markdown(f"🔥 **Total estimasi kalori dari piring ini: {total_kalori} kcal**")

# Plot grafik kebutuhan protein
def plot_protein_chart(dasar, tambahan_goal, tambahan_condition):
    labels = ['Dasar', 'Tujuan', 'Kondisi Medis']
    values = [dasar, tambahan_goal, tambahan_condition]
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['skyblue', 'orange', 'lightgreen'])
    ax.set_ylabel("Gram Protein")
    ax.set_title("Komponen Kebutuhan Protein Harian")
    st.pyplot(fig)

# Ekspor hasil ke Excel
def export_result_to_excel(total, dasar, tambahan_goal, tambahan_condition):
    data = {
        "Komponen": ["Dasar", "Tujuan", "Kondisi Medis", "Total"],
        "Protein (gram)": [dasar, tambahan_goal, tambahan_condition, total]
    }
    df = pd.DataFrame(data)
    df.to_excel("hasil_protein.xlsx", index=False)
    with open("hasil_protein.xlsx", "rb") as file:
        st.download_button("📥 Unduh hasil ke Excel", file, file_name="hasil_protein.xlsx")

# Fungsi utama Streamlit
def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")
    st.markdown("""
        <style>
        .stApp {background-color: #E6CCF5; font-family: 'Comic Sans MS'; color: black;}
        div.stButton > button:first-child {background-color: #FFA500; color: white;}
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
            'Sedentary (tidak aktif)', 'Moderate (cukup aktif)', 'Active (sangat aktif)'])
        goal = st.selectbox('🎯 Apa tujuan Anda?', [
            'Menurunkan berat badan', 'Mempertahankan berat badan', 'Meningkatkan massa otot', 'Menambah berat badan'])
        medical_condition = st.selectbox('🩺 Kondisi Medis (jika ada):', [
            'Tidak ada', 'Hamil (Trimester 1)', 'Hamil (Trimester 2)', 'Hamil (Trimester 3)',
            'Penyakit ginjal ringan', 'Diabetes tipe 2', 'Hipertensi', 'Luka pasca operasi', 'Malnutrisi'])

        if st.button("✅ OK, Hitung Kebutuhan Protein"):
            total, dasar, tambahan_goal, tambahan_condition = calculate_protein_requirement(
                weight, activity_level, gender, age, goal, medical_condition
            )

            with st.expander("📊 Lihat Hasil Perhitungan Kebutuhan Protein Anda"):
                st.success(f"🍗 Kebutuhan protein harian Anda untuk *{goal.lower()}* adalah sekitar *{total:.1f} gram* per hari! 😋")
                st.markdown(f"""
                    <ul>
                    <li>Berat badan: {weight} kg</li>
                    <li>Tinggi badan: {height} cm</li>
                    <li>Usia: {age} tahun</li>
                    <li>Jenis kelamin: {gender}</li>
                    <li>Tingkat aktivitas: {activity_level}</li>
                    <li>Kondisi medis: {medical_condition}</li>
                    </ul>
                """, unsafe_allow_html=True)
                plot_protein_chart(dasar, tambahan_goal, tambahan_condition)
                show_food_recommendations()
                show_protein_plate_simulation(total)
                export_result_to_excel(total, dasar, tambahan_goal, tambahan_condition)

    elif menu == 'Tentang Aplikasi':
        st.header("Tentang Aplikasi")
        st.markdown("""
            Aplikasi ini membantu menghitung kebutuhan protein harian Anda berdasarkan berat badan,
            usia, jenis kelamin, aktivitas, tujuan, dan kondisi medis khusus.
            
            Dibuat dengan Streamlit dan Python.
        """)
        show_avocado_image("avocado.webp")
        autoplay_audio("tap.mp3")

    else:
        st.header("Perkenalan Kelompok")
        st.markdown("""
            **Kelompok 6**  
            - Anggota 1  
            - Anggota 2  
            - Anggota 3  
            - Anggota 4  
        """)

if __name__ == '__main__':
    main()
