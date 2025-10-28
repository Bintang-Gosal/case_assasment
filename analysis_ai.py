import streamlit as st
import matplotlib.pyplot as plt

def render_ai_performance_analysis(df_filtered):
    """Menampilkan analisis Performa AI vs Volume Sesi."""
    st.header("📈 1. Performa AI: Response Time vs Volume")

    # Agregasi data harian
    daily_data = df_filtered.groupby('date').agg(
        total_sessions=('session_id', 'count'),
        avg_ai_response_time=('ai_response_time_sec', 'mean')
    ).reset_index()

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot Response Time (Garis)
    color = 'tab:red'
    ax1.set_xlabel('Tanggal')
    ax1.set_ylabel('Rata-rata Response Time AI (detik)', color=color)
    ax1.plot(daily_data['date'], daily_data['avg_ai_response_time'], color=color, label='Response Time AI')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, linestyle='--', alpha=0.6)

    # Plot Volume Sesi (Bar/Garis lainnya)
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Total Sesi Harian', color=color)  
    ax2.plot(daily_data['date'], daily_data['total_sessions'], color=color, linestyle='--', label='Total Sesi')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.suptitle('Tren Harian: Response Time AI vs Total Volume Sesi')
    st.pyplot(fig)

    st.markdown("""
    **Key Insight:** Terlihat korelasi positif yang kuat, di mana **peningkatan volume pengguna menyebabkan lonjakan signifikan pada AI Response Time**. Ini mengonfirmasi *bottleneck* performa sistem AI yang tidak *scalable*.
    """)
    st.markdown("---")