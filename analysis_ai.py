import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.ticker as ticker # Diperlukan untuk penyesuaian axis

def render_ai_performance_analysis(df):
    """Menampilkan analisis korelasi antara User Traffic dan AI Response Time menggunakan Matplotlib."""
    st.header("1. 🧠 Performa dan Skalabilitas AI")
    st.markdown("Analisis ini mengukur elastisitas AI dalam menghadapi lonjakan User Traffic.")
    
    # Data Aggregation
    df_agg = df.groupby('hour').agg(
        avg_response_time=('ai_response_time_sec', 'mean'),
        total_sessions=('session_id', 'count')
    ).reset_index()

    # Hitung Response Time Tertinggi vs Terendah (Metrics)
    max_rt = df_agg['avg_response_time'].max()
    min_rt = df_agg['avg_response_time'].min()
    
    plt.style.use('seaborn-v0_8-whitegrid') 
    fig, ax1 = plt.subplots(figsize=(12, 6)) # Ukuran figure

    color_sesi = '#4c78a8' # Biru untuk Bar (Sesi)
    color_rt = '#e74c3c'   # Merah untuk Line (Response Time)

    ax1.bar(
        df_agg['hour'], 
        df_agg['total_sessions'], 
        color=color_sesi, 
        alpha=0.7, # Sedikit transparansi agar grid terlihat
        label='Total Sesi', 
        width=0.8
    )
    ax1.set_xlabel('Jam (0-23)', fontsize=12)
    ax1.set_ylabel('Total Sesi', color=color_sesi, fontsize=12, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=color_sesi)
    ax1.set_xticks(np.arange(0, 24, 2)) 
    ax1.set_xlim(-1, 24) 
    ax1.grid(axis='y', linestyle='--', alpha=0.5) 
    ax1.set_axisbelow(True) 

    ax2 = ax1.twinx()  
    
    ax2.plot(
        df_agg['hour'], 
        df_agg['avg_response_time'], 
        color=color_rt, 
        marker='o', 
        linestyle='-', 
        linewidth=3, 
        label='Avg. Response Time (detik)',
        markersize=6
    )
    ax2.set_ylabel('Avg. Response Time (detik)', color=color_rt, fontsize=12, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor=color_rt)
    ax2.set_ylim(bottom=0)

    # Judul dan Legend Gabungan
    fig.suptitle('Korelasi Traffic Jam (Sesi) vs. Average AI Response Time', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    # Menggabungkan legend dari kedua axis
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='upper center', 
               bbox_to_anchor=(0.5, 1.15), ncol=2, frameon=False, fontsize=10) 
    
    fig.tight_layout(rect=[0, 0, 1, 0.95]) # Penyesuaian layout
    
    # Tampilkan di Streamlit
    st.pyplot(fig) 
    plt.close(fig) 

    st.markdown("""
    Key Insight: Bottleneck Akibat Pergeseran Beban Kerja (Manusia ke AI).Meskipun **Total Sesi** terlihat relatif datar, **AI Response Time melonjak tajam di sekitar jam 18:00**. Lonjakan ini kemungkinan besar disebabkan oleh **berkurangnya ketersediaan Konselor Manusia** pada akhir jam kerja, memaksa sistem mengalihkan **semua beban dan kasus yang lebih kompleks** kepada AI. 
    Kenaikan dramatis *Response Time* menunjukkan bahwa infrastruktur AI **gagal menskalakan atau mengelola kompleksitas kasus** yang diwariskan dari tim manusia, bukan hanya *traffic* volume murni.
    """)
    st.markdown("---")
