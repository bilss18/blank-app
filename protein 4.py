import streamlit as st
import matplotlib.pyplot as plt

# Fungsi hitung kebutuhan protein
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

# Daftar makanan dan info protein
food_list = {
    "Tempe (100g)": 19,
    "Telur rebus (1 butir)": 6,
    "Ikan lele goreng (100g)": 20,
    "Dada ayam rebus (100g)": 31,
    "Susu kedelai (1 gelas)": 7,
    "Tahu putih (100g)": 10
}

def show_food_recommendations():
    st.markdown("### 🍽 Rekomendasi Makanan Lokal Tinggi Protein:")
    for food, protein in food_list.items():
        st.write(f"- **{food}**: {protein}g protein")

def show_protein_plate_simulation(target_protein):
    st.markdown("### 🍱 Simulasi Piring Protein:")
    remaining = target_protein
    selected = []
    for food, protein in food_list.items():
        if remaining <= 0:
            break
        qty = int(remaining // protein)
        if qty > 0:
            selected.append((qty, food, qty * protein))
            remaining -= qty * protein
    for qty, food, total_protein in selected:
        st.write(f"- {qty}x {food} = {total_protein}g protein")
    if remaining > 0:
        st.write(f"Sisa {remaining:.1f}g protein, bisa dilengkapi dengan camilan tinggi protein.")

def plot_protein_chart(dasar, goal, medical):
    labels = ['Dasar', 'Tujuan', 'Kondisi Medis']
    values = [dasar, goal, medical]
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['skyblue', 'orange', 'lightgreen'])
    ax.set_ylabel('Gram Protein')
    ax.set_title('Komponen Kebutuhan Protein Harian')
    st.pyplot(fig)

def main():
    st.title("🍳 Kalkulator Kebutuhan Protein Harian")

    age = st.number_input("Umur (tahun):", min_value=1, step=1)
    gender = st.selectbox("Jenis Kelamin:", ['Laki-laki', 'Perempuan'])
    weight = st.number_input("Berat badan (kg):", min_value=1.0, step=0.1)
    activity_level = st.selectbox("Tingkat Aktivitas:", [
        'Sedentary (tidak aktif)', 'Moderate (cukup aktif)', 'Active (sangat aktif)'
    ])
    goal = st.selectbox("Tujuan:", [
        'Menurunkan berat badan', 'Mempertahankan berat badan', 'Meningkatkan massa otot', 'Menambah berat badan'
    ])
    medical_condition = st.selectbox("Kondisi Medis (jika ada):", [
        'Tidak ada', 'Hamil (Trimester 1)', 'Hamil (Trimester 2)', 'Hamil (Trimester 3)',
        'Penyakit ginjal ringan', 'Diabetes tipe 2', 'Hipertensi', 'Luka pasca operasi', 'Malnutrisi'
    ])

    if st.button("Hitung Kebutuhan Protein"):
        total, dasar, tambahan_goal, tambahan_medical = calculate_protein_requirement(
            weight, activity_level, gender, age, goal, medical_condition
        )
        st.success(f"Kebutuhan protein harian Anda: **{total:.1f} gram**")
        plot_protein_chart(dasar, tambahan_goal, tambahan_medical)
        show_food_recommendations()
        show_protein_plate_simulation(total)

if __name__ == "__main__":
    main()
