import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Fungsi hitung kebutuhan protein harian
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

# Data makanan lokal dengan (protein, kalori, keterangan)
food_list = {
    "Tempe (100g)": (19, 192, "Sumber protein nabati tinggi, murah dan mudah didapat."),
    "Telur rebus (1 butir)": (6, 78, "Protein hewani cepat saji dan padat gizi."),
    "Ikan lele goreng (100g)": (20, 180, "Kaya omega-3 dan protein tinggi."),
    "Dada ayam rebus (100g)": (31, 165, "Protein tinggi, rendah lemak."),
    "Susu kedelai (1 gelas)": (7, 100, "Sumber protein cair nabati."),
    "Tahu putih (100g)": (10, 76, "Serbaguna untuk berbagai masakan.")
}

def show_food_recommendations():
    st.markdown("🍽 **Rekomendasi Makanan Lokal Tinggi Protein:**")
    for name, (protein, kalori, note) in food_list.items():
        st.markdown(f"- **{name}**: {protein}g protein, {kalori} kcal — _{note}_")

def show_protein_plate_simulation(target_protein):
    st.markdown("🍱 **Simulasi Piring Protein:**")
    remaining = target_protein
    selected = []
    total_kalori = 0

    for name, (protein, kalori, _) in food_list.items():
        if remaining <= 0:
            break
        qty = int(remaining // protein)
        if qty > 0:
            total_protein = qty * protein
            total_kal = qty * kalori
            selected.append((qty, name, total_protein, total_kal))
            total_kalori += total_kal
            remaining -= total_protein

    for qty, name, protein_sum, kal_sum in selected:
        st.markdown(f"- {qty}x **{name}** → {protein_sum:.1f}g protein, {kal_sum} kcal")

    if remaining > 0:
        st.markdown(f"🔹 Sisa {remaining:.1f}g protein bisa dilengkapi dengan camilan tinggi protein.")

    st.markdown(f"🔥 **Total estimasi kalori dari piring ini: {total_kalori} kcal**")

def plot_protein_chart(dasar, goal, medical):
    labels = ['Dasar', 'Tujuan', 'Kondisi Medis']
    values = [dasar, goal, medical]
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['skyblue', 'orange', 'lightgreen'])
    ax.set_ylabel('Gram Protein')
    ax.set_title('Komponen Kebutuhan Protein Harian')
    st.pyplot(fig)

def main():
    st.set_page_config(page_title="Kalkulator Protein", layout="centered")
    st.title("🍳 Kalkulator Kebutuhan Protein Harian")

    age = st.number_input("📅 Masukkan umur Anda (tahun):", min_value=1, step=1)
    gender = st.selectbox("🚻 Pilih jenis kelamin Anda:", ['Laki-laki', 'Perempuan'])
    height = st.number_input("📏 Masukkan tinggi badan Anda (cm):", min_value=50, step=1)
    weight = st.number_input("⚖ Masukkan berat badan Anda (kg):", min_value=1.0, step=0.1)

    activity_level = st.selectbox("🏃‍♀ Pilih tingkat aktivitas Anda:", [
        'Sedentary (tidak aktif)', 'Moderate (cukup aktif)', 'Active (sangat aktif)'
    ])
    goal = st.selectbox("🎯 Apa tujuan Anda?", [
        'Menurunkan berat badan', 'Mempertahankan berat badan', 'Meningkatkan massa otot', 'Menambah berat badan'
    ])
    medical_condition = st.selectbox("🩺 Kondisi Medis (jika ada):", [
        'Tidak ada', 'Hamil (Trimester 1)', 'Hamil (Trimester 2)', 'Hamil (Trimester 3)',
        'Penyakit ginjal ringan', 'Diabetes tipe 2', 'Hipertensi', 'Luka pasca operasi', 'Malnutrisi'
    ])

    if st.button("✅ Hitung Kebutuhan Protein"):
        total, dasar, tambahan_goal, tambahan_condition = calculate_protein_requirement(
            weight, activity_level, gender, age, goal, medical_condition
        )

        st.success(f"Kebutuhan protein harian Anda untuk *{goal.lower()}* adalah sekitar **{total:.1f} gram** per hari!")
        st.markdown(f"""
        - Berat badan: {weight} kg  
        - Tinggi badan: {height} cm  
        - Umur: {age} tahun  
        - Jenis kelamin: {gender}  
        - Tingkat aktivitas: {activity_level}  
        - Kondisi medis: {medical_condition}
        """)
        plot_protein_chart(dasar, tambahan_goal, tambahan_condition)
        show_food_recommendations()
        show_protein_plate_simulation(total)

if __name__ == "__main__":
    main()
