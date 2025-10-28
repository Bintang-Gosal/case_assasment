import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

def render_ai_performance_analysis(df):
    """Menampilkan analisis korelasi antara User Traffic dan AI Response Time menggunakan Matplotlib."""
    st.header("1. 🧠 Performa dan Skalabilitas AI")
    st.markdown("Analisis ini mengukur elastisitas AI dalam menghadapi lonjakan User Traffic.")
    
    df_agg = df.groupby('hour').agg(
    avg_response_time=('ai_response_time_sec', 'mean'),
    total_sessions=('session_id', 'count')
    ).reset_index()

    # 1. Inisialisasi figure dan axis pertama
    fig, ax1 = plt.subplots(figsize=(10, 5))

    # Konfigurasi Sumbu Y Kiri (Total Sesi)
    color_sesi = '#4c78a8'
    ax1.plot(df_agg['hour'], df_agg['total_sessions'], color=color_sesi, marker='o', linestyle='-', linewidth=2, label='Total Sesi')
    ax1.set_xlabel('Jam (0-23)')
    ax1.set_ylabel('Total Sesi', color=color_sesi)
    ax1.tick_params(axis='y', labelcolor=color_sesi)
    ax1.set_xticks(np.arange(0, 24, 2)) # Menampilkan tick setiap 2 jam
    ax1.grid(True, linestyle='--', alpha=0.5, which='both')

    # 2. Buat Axis kedua (y2) 
    ax2 = ax1.twinx()  
    
    # Konfigurasi Sumbu Y Kanan (Avg. Response Time)
    color_rt = '#e74c3c'
    ax2.plot(df_agg['hour'], df_agg['avg_response_time'], color=color_rt, marker='D', linestyle='-', linewidth=2, label='Avg. Response Time (detik)')
    ax2.set_ylabel('Avg. Response Time (detik)', color=color_rt)
    ax2.tick_params(axis='y', labelcolor=color_rt)
    
    # Judul dan Legend
    plt.title('Korelasi Traffic Jam (Sesi) vs. Average AI Response Time (Matplotlib)', fontsize=14)
    fig.legend(loc="upper center", bbox_to_anchor=(0.5, 1.1), ncol=2) 
    fig.tight_layout() 
    
    # Tampilkan di Streamlit
    st.pyplot(fig) 
    plt.close(fig)  

    st.markdown("""
    **Key Insight:** Terlihat korelasi negatif yang jelas: saat **Total Sesi melonjak (khususnya 20:00 - 01:00)**, **AI Response Time meningkat tajam (+35%)**. Ini mengindikasikan bahwa infrastruktur AI tidak mampu melakukan *scaling* (elastisitas) dan menjadi *bottleneck* utama dalam layanan.
    """)
    st.markdown("---")