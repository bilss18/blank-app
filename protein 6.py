if st.button("✅ OK, Hitung Kebutuhan Protein"):
    total, dasar, tambahan = calculate_protein_requirement(weight, activity_level, gender, age, goal, medical_condition)

    st.success(f"🍗 Kebutuhan protein harian Anda untuk tujuan '{goal}' adalah sekitar {total:.1f} gram per hari! 😋")

    desc_goal = {
        'Menurunkan berat badan': "Pengurangan protein untuk mendukung penurunan berat badan secara sehat.",
        'Mempertahankan berat badan': "Protein dasar untuk menjaga berat badan dan kesehatan otot.",
        'Menambah berat badan ringan': "Penambahan protein ringan untuk meningkatkan berat badan secara bertahap.",
        'Menambah berat badan sedang': "Penambahan protein sedang untuk mendukung peningkatan massa tubuh.",
        'Menambah berat badan banyak': "Penambahan protein signifikan untuk pertumbuhan massa otot dan berat badan.",
        'Menambah berat badan sangat banyak': "Penambahan protein maksimal untuk mempercepat peningkatan berat badan."
    }

    st.markdown(f"**Keterangan:** {desc_goal[goal]}")

    st.markdown(f"""
        <ul>
        <li>Berat badan: {weight} kg</li>
        <li>Tinggi badan: {height} cm</li>
        <li>Kebutuhan dasar: {dasar:.1f} gram</li>
        <li>Penyesuaian karena tujuan & kondisi medis: {tambahan:+.1f} gram</li>
        </ul>
    """, unsafe_allow_html=True)

    show_avocado_image("avocado.gif")  # tampilkan avocado GIF di sini
    show_food_recommendations()
    show_protein_plate()
