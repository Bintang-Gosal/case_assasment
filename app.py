import streamlit as st
import pandas as pd
from data_loader import load_and_preprocess_data
from analysis_ai import render_ai_performance_analysis
from analysis_satisfaction import render_satisfaction_analysis
from analysis_counselor import render_counselor_allocation_analysis
from reporting import render_summary_and_recommendations

# Konfigurasi dan Pemanggilan Data 
st.set_page_config(layout="wide", page_title="EmergencyyCall Operational Analytics")

# Memuat data dan menangkap statistik cleansing (DataFrame dan Dict)
df, cleansing_stats = load_and_preprocess_data('case_assessment_data.csv')

if df.empty:
    st.stop() # Hentikan aplikasi jika data gagal dimuat

# Judul dan Filter
st.title("💡 EmergencyyCall: Operational & User Insight")

# Author
st.caption(f"Laporan Analisis Performa Layanan - September 2025 | Dibuat oleh: **Bintang Fridel Putra**")

st.markdown("Analisis Performa Layanan dan Pengguna")

st.sidebar.header("Filter Data")
# Tanggal
date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal", 
    value=(df['date'].min(), df['date'].max()), 
    min_value=df['date'].min(), 
    max_value=df['date'].max()
)

if len(date_range) == 2:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])
    df_filtered = df[(df['date'] >= start_date) & (df['date'] <= end_date)].copy()
else:
    df_filtered = df.copy()

# Ringkasan Metrik Kunci
st.subheader("Ringkasan Metrik Kunci")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sesi Siap Analisis", df_filtered.shape[0])
col2.metric("Rata-rata Response Time AI (detik)", f"{df_filtered['ai_response_time_sec'].mean():.2f}")
col3.metric("Rata-rata Kepuasan Pengguna (1-5)", f"{df_filtered['user_satisfaction_score'].mean():.2f}")
col4.metric("Persentase Ketersediaan Konselor", f"{df_filtered['counselor_available'].mean() * 100:.1f}%")

st.markdown("---")

# Menampilkan Analisis dari Setiap Modul
render_ai_performance_analysis(df_filtered)
render_satisfaction_analysis(df_filtered)
render_counselor_allocation_analysis(df_filtered)

# Menampilkan Ringkasan dan Rekomendasi 
render_summary_and_recommendations()

# FUNGSI UNTUK MENAMPILKAN LOG DATA CLEANSING
def display_cleansing_log(stats):
    total_rows_raw = stats['total_raw']
    total_cleaned = stats['total_cleaned']
    
    st.markdown("---")
    st.header("🔬 Detail Log Pembersihan Data (Audit Trail)")
    
    with st.expander(f"Lihat {total_rows_raw - total_cleaned} Baris yang Dihapus ({total_rows_raw} Baris Awal)"):
        st.subheader("Rincian Proses Data Cleansing")
        
        # Tabel Ringkasan
        data_ringkas = {
            'Langkah Pembersihan': ['Duplikasi Sesi', 'Missing Reports', 'Nilai NULL Kualitas'],
            'Baris Dihapus': [
                stats['removed_duplicate'],
                stats['removed_missing'],
                stats['removed_null']
            ],
            'Persentase Total Raw': [
                stats['removed_duplicate'] / total_rows_raw,
                stats['removed_missing'] / total_rows_raw,
                stats['removed_null'] / total_rows_raw
            ]
        }
        df_log = pd.DataFrame(data_ringkas)
        df_log['Persentase Total Raw'] = df_log['Persentase Total Raw'].apply(lambda x: f"{x:.2%}")
        st.dataframe(df_log, hide_index=True)

        st.metric("Total Sesi Awal", total_rows_raw)
        st.metric("Total Sesi Siap Analisis", total_cleaned)
        
# Panggil fungsi display log di bagian paling bawah
display_cleansing_log(cleansing_stats)
