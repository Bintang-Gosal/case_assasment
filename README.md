## EmergencyyCall: Operational & User Insight Dashboard

### Gambaran Umum Proyek
Dashboard ini dikembangkan untuk menganalisis performa operasional platform layanan kesehatan mental EmergencyyCall, dengan fokus pada korelasi antara User Traffic, Kapasitas AI, dan Alokasi Sumber Daya Konselor.
Tujuan utama dari analisis ini adalah untuk mengidentifikasi akar masalah di balik penurunan kepuasan pengguna (-15%) dan memberikan rekomendasi strategis berbasis data.

### Key Insights Utama

- AI Gagal Skala (Scaling): Peningkatan User Traffic (+28%) menyebabkan lonjakan AI Response Time (+35%), yang membuktikan bahwa infrastruktur AI tidak elastis.

- Krisis Malam Hari: Kepuasan pengguna terburuk terjadi pada malam hari (21:00 - 02:00), di mana Response Time AI tinggi dan Antrian Konselor meledak.

- Mismatched Allocation: Alokasi Konselor bersifat statis dan gagal menyesuaikan diri dengan puncak permintaan malam hari.
  
---

### Persyaratan

Pastikan lingkungan Python Anda memiliki library berikut:

- pandas
- streamlit
- matplotlib

### Cara Menjalankan Dashboard

1. Pastikan semua file Python dan case_assessment_data.csv berada dalam direktori yang sama.
2. Buka terminal atau Command Prompt Anda di direktori proyek.
3. Jalankan perintah berikut: (**streamlit run app.py**)
