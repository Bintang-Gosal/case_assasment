import pandas as pd
import streamlit as st

@st.cache_data
def load_and_preprocess_data(file_path):
    """Memuat data dari CSV, membersihkan, dan melakukan rekayasa fitur dasar."""
    try:
        df = pd.read_csv(file_path, delimiter=';')
    except FileNotFoundError:
        st.error(f"File {file_path} tidak ditemukan. Pastikan file ada di direktori yang sama.")
        return pd.DataFrame(), {} # Kembalikan DataFrame kosong dan Dict kosong

    # Kode pembersihan tipe data dan rekayasa fitur lainnya tetap sama) 
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%m/%Y %H:%M')
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    df['ai_response_time_sec'] = df['ai_response_time_ms'] / 1000 
    df['time_of_day'] = df['hour'].apply(lambda x: 'Night' if x >= 18 or x < 6 else 'Day')
    
    total_rows_raw = len(df)
    
    # A. Menghapus Duplikasi Sesi
    df_cleaned = df[df['duplicate_flag'] == False].copy()
    rows_removed_duplicate = total_rows_raw - len(df_cleaned)
    
    # B. Menghapus Missing Report
    rows_before_missing_drop = len(df_cleaned)
    df_cleaned = df_cleaned[df_cleaned['missing_report_flag'] == False].copy()
    rows_removed_missing = rows_before_missing_drop - len(df_cleaned)

    # C. Menghapus NULL 
    rows_before_null_drop = len(df_cleaned)
    df_cleaned.dropna(subset=['user_satisfaction_score', 'ai_accuracy'], inplace=True)
    rows_removed_null = rows_before_null_drop - len(df_cleaned)
    
    cleansing_stats = {
        'total_raw': total_rows_raw,
        'removed_duplicate': rows_removed_duplicate,
        'removed_missing': rows_removed_missing,
        'removed_null': rows_removed_null,
        'total_cleaned': len(df_cleaned)
    }

    return df_cleaned, cleansing_stats