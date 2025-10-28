import streamlit as st

def render_summary_and_recommendations():
    """Menampilkan Ringkasan Temuan Utama dan Rekomendasi Strategis."""
    st.header("📝 Ringkasan Temuan Utama (Key Insights)")

    st.error("""
    Analisis mengonfirmasi adanya **Krisis Kapasitas di Jam Puncak (Malam Hari)**, di mana peningkatan User Traffic (+28%) tidak diimbangi oleh skalabilitas sistem dan alokasi sumber daya.
    
    1.  **AI Gagal Scaling dan Memicu Krisis:** **AI Response Time meningkat signifikan (+35%)** seiring lonjakan volume sesi. Kegagalan kapasitas teknis AI ini secara langsung memicu **penurunan tajam Kepuasan Pengguna Malam Hari (-15%)**.
    2.  **Kesenjangan Alokasi Sumber Daya Manusia:** Alokasi konselor **tidak adaptif** dan cenderung datar. Puncak antrian konselor terjadi di jam **21:00 hingga 01:00**, menunjukkan bahwa kegagalan AI memaksa pengguna beralih, namun Konselor tidak tersedia dalam jumlah yang cukup.
    3.  **Dampak Domino:** Seluruh masalah berasal dari **ketidaksesuaian waktu** antara permintaan dan kapasitas. Pengguna krisis tidak dilayani dengan cepat oleh AI maupun Konselor, mengancam retensi jangka panjang.
    4.  **Integritas Data (Latar Belakang):** Walaupun telah dibersihkan dalam proses *loading*, sistem log masih menunjukkan anomali (Duplikasi dan Missing Report), menandakan **risiko akurasi data** tetap tinggi tanpa perbaikan sistem permanen.
    """)

    st.header("🎯 Rekomendasi Strategis Berbasis Data")

    st.success("""
    ### Jangka Pendek (Mitigasi Risiko dalam 1-4 Minggu)
    * **Pembaruan Penjadwalan Konselor (Quick Win):** Segera terapkan **penjadwalan konselor yang diubah 30%** untuk mencakup jam puncak **20:00 - 02:00**. Alihkan alokasi dari shift *idle* siang hari ke shift malam untuk segera mengurangi *queue length*.
    * **Triage Prioritas Cepat:** Implementasikan *triage* cerdas: Jika AI Response Time terdeteksi melebihi **2.0 detik** (ambang batas kepuasan), sesi harus secara otomatis **diprioritaskan** untuk dialihkan ke Konselor yang tersedia (mode *Hybrid*).

    ### Jangka Menengah (Optimalisasi Sistem dalam 1-3 Bulan)
    * **Peningkatan Kapasitas AI (Scaling):** Tim Engineering harus segera melakukan **Horizontal Scaling** infrastruktur server AI. Targetkan Response Time AI di bawah **1.0 detik** di semua kondisi *traffic* untuk memulihkan kepuasan malam hari.
    * **Perbaikan Permanen Logging Sistem:** Audit dan perbaiki *logging pipeline* (ETL) secara permanen untuk mengeliminasi Duplikasi Sesi dan Missing Report pada sumber data. Ini adalah **prasyarat** untuk semua proyek kuartal berikutnya.

    ### Jangka Panjang (Perencanaan Sistem Baru Kuartal Depan)
    * **Implementasi Dynamic Resource Allocation (DRA):** Kembangkan model prediktif berbasis *time-series* untuk meramalkan *user traffic* 3 jam ke depan. Gunakan DRA untuk **menyesuaikan jumlah *instance* server AI dan alokasi Konselor secara *real-time***, menciptakan sistem yang adaptif dan *scalable*.
    """)