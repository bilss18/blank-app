import streamlit as st
import pandas as pd

# Fungsi hitung protein harian
def calculate_protein(weight, activity_level, gender, age, goal, medical_condition):
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
        'Diabetes tipe 2': 0,
        'Hipertensi': 0,
        'Luka pasca operasi': 0.3,
        'Malnutrisi': 0.4
    }

    dasar = weight * (multiplier[activity_level] + gender_age_adj)
    tambahan_goal = weight * goal_adj[goal]
    tambahan_medical = weight * medical_adj[medical_condition]
    total = dasar + tambahan_goal + tambahan_medical
    return total, dasar, tambahan_goal, tambahan_medical

# Daftar makanan lokal tinggi protein
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

def main():
    st.title('🍳 Kalkulator Kebutuhan Protein Harian')

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
        total, dasar, goal_adj, med_adj = calculate_protein(weight, activity_level, gender, age, goal, medical_condition)
        st.success(f"Kebutuhan protein harian Anda: **{total:.1f} gram**")
        st.write(f"- Kebutuhan dasar: {dasar:.1f} gram")
        st.write(f"- Penyesuaian tujuan: {goal_adj:+.1f} gram")
        st.write(f"- Penyesuaian medis: {med_adj:+.1f} gram")
        show_food_recommendations()

if __name__ == '__main__':
    main()
