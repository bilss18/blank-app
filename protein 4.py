import streamlit as st

# Fungsi hitung kebutuhan protein
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
        'Malnutrisi': 0.4,
        'Penyakit jantung': -0.1,
        'Asma': 0.05
    }

    dasar = weight * (multiplier[activity_level] + gender_age_adj)
    tambahan_goal = weight * goal_adj[goal]
    tambahan_medical = weight * medical_adj[medical_condition]
    total = dasar + tambahan_goal + tambahan_medical
    return total, dasar, tambahan_goal, tambahan_medical

# Data makanan lokal tinggi protein
food_list = {
    "Tempe (100g)": (19, "Sumber protein nabati tinggi, murah dan mudah didapat."),
    "Telur rebus (1 butir)": (6, "Protein hewani cepat saji dan padat gizi."),
    "Ikan lele goreng (100g)": (20, "Kaya omega-3 dan protein tinggi."),
    "Dada ayam rebus (100g)": (31, "Protein tinggi, rendah lemak."),
    "Susu kedelai (1 gelas)": (7, "Sumber protein cair nabati."),
    "Tahu putih (100g)": (10, "Serbaguna untuk berbagai masakan.")
}

def show_food_recommendations():
    st.markdown("### 🍽 Rekomendasi Makanan Lokal Tinggi Protein:")
    for name, (protein, note) in food_list.items():
        st.markdown(f"- **{name}**: {protein}g protein — _{note}_")

def show_protein_plate_simulation(target_protein):
    st.markdown("### 🍱 Simulasi Piring Protein:")
    remaining = target_protein
    selections = []
    for name, (protein, _) in food_list.items():
        if remaining <= 0:
            break
        qty = int(remaining // protein)
        if qty > 0:
            protein_total = protein * qty
            selections.append((qty, name, protein_total))
            remaining -= protein_total
    for qty, name, protein_total in selections:
        st.write(f"- {qty}x **{name}** → {protein_total:.1f}g protein")
    if remaining > 0:
        st.write(f"⚠️ Sisa kebutuhan protein sekitar {remaining:.1f}g, bisa dilengkapi dengan camilan kaya protein.")

def main():
    st.title("🍳 Kalkulator Kebutuhan Protein Harian")

    st.sidebar.header("Input Data Anda")
    age = st.sidebar.number_input("Umur (tahun)", min_value=1, max_value=120, value=25)
    gender = st.sidebar.selectbox("Jenis Kelamin", ['Laki-laki', 'Perempuan'])
    height = st.sidebar.number_input("Tinggi badan (cm)", min_value=50, max_value=250, value=170)
    weight = st.sidebar.number_input("Berat badan (kg)", min_value=10.0, max_value=300.0, value=60.0, step=0.1)
    activity_level = st.sidebar.selectbox("Tingkat Aktivitas", [
        'Sedentary (tidak aktif)',
        'Moderate (cukup aktif)',
        'Active (sangat aktif)'
    ])
    goal = st.sidebar.selectbox("Tujuan", [
        'Menurunkan berat badan',
        'Mempertahankan berat badan',
        'Meningkatkan massa otot',
        'Menambah berat badan'
    ])
    medical_condition = st.sidebar.selectbox("Kondisi Medis (jika ada)", [
        'Tidak ada',
        'Hamil (Trimester 1)',
        'Hamil (Trimester 2)',
        'Hamil (Trimester 3)',
        'Penyakit ginjal ringan',
        'Diabetes tipe 2',
        'Hipertensi',
        'Luka pasca operasi',
        'Malnutrisi',
        'Penyakit jantung',
        'Asma'
    ])

    if st.sidebar.button("Hitung Kebutuhan Protein"):
        total, dasar, goal_adj, med_adj = calculate_protein(weight, activity_level, gender, age, goal, medical_condition)
        st.success(f"**Kebutuhan protein harian Anda: {total:.1f} gram**")
        st.write(f"- Kebutuhan dasar: {dasar:.1f} gram")
        st.write(f"- Penyesuaian karena tujuan: {goal_adj:+.1f} gram")
        st.write(f"- Penyesuaian karena kondisi medis: {med_adj:+.1f} gram")
        
        show_food_recommendations()
        show_protein_plate_simulation(total)

if __name__ == "__main__":
    main()
