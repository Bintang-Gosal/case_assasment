import streamlit as st
import matplotlib.pyplot as plt

def render_counselor_allocation_analysis(df_filtered):
    """Menampilkan analisis Alokasi Sumber Daya Konselor & Antrian."""
    st.header("👥 3. Alokasi Sumber Daya Konselor & Antrian")

    # Agregasi data per jam
    counselor_data = df_filtered.groupby('hour').agg(
        avg_queue_length=('counselor_queue_length', 'mean'),
        avg_counselors_on_shift=('counselors_on_shift', 'mean')
    ).reset_index()

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot Antrian (Bar)
    ax1.bar(counselor_data['hour'], counselor_data['avg_queue_length'], color='orange', alpha=0.6, label='Rata-rata Antrian')
    ax1.set_xlabel('Jam (0-23)')
    ax1.set_ylabel('Rata-rata Panjang Antrian', color='orange')
    ax1.tick_params(axis='y', labelcolor='orange')
    ax1.set_xticks(range(24))

    # Plot Konselor (Garis)
    ax2 = ax1.twinx()
    ax2.plot(counselor_data['hour'], counselor_data['avg_counselors_on_shift'], color='green', marker='o', label='Rata-rata Konselor Shift')
    ax2.set_ylabel('Rata-rata Konselor Tugas', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    fig.suptitle('Ketidakseimbangan Antrian Konselor vs. Alokasi Shift')
    st.pyplot(fig)

    st.markdown("""
    **Key Insight:** Terjadi **ketidakseimbangan alokasi**. Puncak antrian di malam hari (00:00 - 05:00) tidak diikuti oleh peningkatan jumlah konselor yang signifikan. Alokasi konselor manusia menurun pada jam malam, mengabaikan **puncak permintaan *user* malam hari**.
    """)

