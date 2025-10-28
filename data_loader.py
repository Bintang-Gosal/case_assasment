import pandas as pd
import streamlit as st

@st.cache_data
def load_and_preprocess_data(file_path):
    """Memuat data dari CSV, membersihkan, dan melakukan rekayasa fitur dasar."""
    try:
        # Pengecekan File (Error Deployment/Path)
        df = pd.read_csv(file_path, delimiter=';')
    except FileNotFoundError:
        st.error(f"❌ KESALAHAN KRITIS: File '{file_path}' tidak ditemukan. Pastikan file data sudah di-commit dan terunggah di repositori Git.")
        # Mengembalikan DataFrame kosong dan Dict kosong
        return pd.DataFrame(), {} 
    except Exception as e:
        # Pengecekan Error Membaca CSV lainnya (Permission, dll.)
        st.error(f"❌ KESALAHAN MEMBACA FILE: Gagal membaca CSV. Detail: {e}")
        return pd.DataFrame(), {} 

    try:
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%m/%Y %H:%M', errors='coerce')
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y', errors='coerce')
        df['ai_response_time_sec'] = df['ai_response_time_ms'] / 1000 
        df['time_of_day'] = df['hour'].apply(lambda x: 'Night' if x >= 18 or x < 6 else 'Day')

        # Data Cleansing dan Perhitungan Statistik
        total_rows_raw = len(df)
        df_cleaned = df[df['duplicate_flag'] == False].copy()
        rows_removed_duplicate = total_rows_raw - len(df_cleaned)
        
        rows_before_missing_drop = len(df_cleaned)
        df_cleaned = df_cleaned[df_cleaned['missing_report_flag'] == False].copy()
        rows_removed_missing = rows_before_missing_drop - len(df_cleaned)

        rows_before_null_drop = len(df_cleaned)
        # Menghapus NULL pada kolom kualitas yang akan digunakan dalam perhitungan
        df_cleaned.dropna(subset=['user_satisfaction_score', 'ai_accuracy'], inplace=True)
        rows_removed_null = rows_before_null_drop - len(df_cleaned)
        
        # Objek Statistik yang akan dikembalikan ke app.py
        cleansing_stats = {
            'total_raw': total_rows_raw,
            'removed_duplicate': rows_removed_duplicate,
            'removed_missing': rows_removed_missing,
            'removed_null': rows_removed_null,
            'total_cleaned': len(df_cleaned)
        }

        # Mengembalikan DataFrame yang bersih dan Statistik Cleansing
        return df_cleaned, cleansing_stats
        
    except Exception as e:
        st.error(f"❌ KESALAHAN PEMROSESAN DATA: Gagal dalam konversi tipe data atau rekayasa fitur. Pastikan format kolom benar. Detail: {e}")
        # KONSISTENSI: Mengembalikan DataFrame kosong dan Dict kosong
        return pd.DataFrame(), {}