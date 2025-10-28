import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def render_satisfaction_analysis(df_filtered):
    """Menampilkan analisis Kepuasan Pengguna Berdasarkan Waktu dan Channel."""
    st.header("🌙 2. Kepuasan Pengguna Berdasarkan Waktu dan Channel")

    # Hitung rata-rata kepuasan per Jam dan Channel
    satisfaction_by_time_channel = df_filtered.groupby(['hour', 'channel'])['user_satisfaction_score'].mean().reset_index()

    # Visualisasi
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=satisfaction_by_time_channel,
        x='hour',
        y='user_satisfaction_score',
        hue='channel',
        marker='o'
    )
    plt.axvspan(18, 23.5, color='gray', alpha=0.2, label='Jam Malam') 
    plt.axvspan(-0.5, 5.5, color='gray', alpha=0.2) 
    plt.title('Rata-rata Kepuasan Pengguna Berdasarkan Jam dan Channel')
    plt.xlabel('Jam (0-23)')
    plt.ylabel('Rata-rata Skor Kepuasan')
    plt.xticks(range(24))
    plt.legend(title='Channel')
    plt.grid(True, linestyle='--', alpha=0.7)
    st.pyplot(fig)

    st.markdown("""
    **Key Insight:** Grafik menunjukkan penurunan skor kepuasan yang tajam pada sesi **AI** selama jam malam (terutama 20:00 - 02:00). Masalah utama kepuasan malam hari ada pada **kualitas interaksi dan kecepatan respon AI**.
    """)
    st.markdown("---")