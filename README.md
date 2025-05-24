# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech (Jaya Jaya Institute)

## Business Understanding
Jaya Jaya Institute merupakan sebuah institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Institusi ini dikenal sebagai penerima siswa dari berbagai macam kalangan dengan memiliki kelas pagi dan malam serta menyediakan lebih dari 10 pilihan jurusan

### Permasalahan Bisnis
Adapun permasalahan bisnis yang dihadapi adalah tingginya Dropout (DO) rate, yang memiliki arti bahwa siswa tidak dapat menyelesaikan pendidikannya. Hal tersebut disebabkan akibat banyaknya jurusan yang harus diawasi dan faktor-faktor lainnya agar mendorong pihak institusi pendidikan untuk mencari penyebab tingginya Dropout rate sehingga dapat mengatasi bahkan meminimalisir terjadinya Dropout di kemudian hari.

### Cakupan Proyek
1. Melakukan analisis faktor apa saja yang mengakibatkan tingginya dropout rate
2. Membuat model machine learning dan simple prediction menggunakan streamlit untuk mengetahui prediksi
3. Membuat dashboard menggunakan streamlit

### Persiapan

Sumber data: [Dataset Student](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment:
```
Berikut langkah-langkah untuk mempersiapkan environment dan akses dashboard:
1. Melakukan install library yang akan digunakan dengan perintah
pip install -r requirements.txt
2. Menjalankan `notebook.ipynb`
   - Pastikan dependensi, packages, library yang dibutuhkan sudah tersedia (lihat file `requirements.txt` untuk melihat dependensi yang dibutuhkan).
   - Jalankan seluruh isi file `notebook.ipynb` menggunakan Google Colab/Jupyter Notebook untuk melihat hasil analisis data, temuan, dan insight yang diperoleh.
3. Buka link Dashboard (bisa dilihat pada link dibawah ini atau run streamlit)
   - 
```

## 📊 Business Dashboard

Dashboard interaktif dibangun menggunakan **Streamlit** dengan tujuan utama:
- Menganalisis penyebab **tingginya angka dropout** mahasiswa.
- Menyediakan visualisasi yang mendalam berdasarkan atribut seperti jurusan, gender, nilai masuk, status keuangan, dan beasiswa.
- Memberikan **alat prediksi** sederhana berbasis Machine Learning untuk membantu pengambilan keputusan akademik.

### Fitur Utama:
- **Filter interaktif** berdasarkan status mahasiswa, jurusan, gender, dan waktu kuliah.
- Visualisasi dropout rate, distribusi nilai semester, status beasiswa, hingga jurusan dengan dropout tertinggi.
- Fitur **prediksi risiko dropout** untuk mahasiswa baru berdasarkan data profil mereka.

🔗 **Akses Dashboard Streamlit (lokal)**: Jalankan dengan perintah:
```bash
streamlit run app.py
```

## 🤖 Menjalankan Sistem Machine Learning

Proyek ini juga menyertakan **prototype sistem prediksi dropout mahasiswa** berbasis model klasifikasi yang telah dilatih dari data historis.

### Cara menjalankan:
1. Pastikan semua dependensi telah diinstall:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan file `app.py`:
   ```bash
   streamlit run app.py
   ```
3. Buka halaman **Prediction** dari sidebar Streamlit.
4. Masukkan profil mahasiswa, lalu tekan tombol **"🔍 Prediksi Sekarang"** untuk melihat hasilnya.

🔍 Model menggunakan beberapa fitur penting:
- Jurusan & waktu kuliah
- Gender & usia masuk
- Status beasiswa, tunggakan biaya, kebutuhan khusus
- Nilai semester 1 dan 2

## ✅ Conclusion

Melalui analisis data dan visualisasi pada dashboard ini, dapat disimpulkan bahwa:
- **Dropout rate cukup tinggi** pada jurusan-jurusan tertentu seperti *Informatics Engineering*, *Tourism*, dan *Social Service*.
- Mahasiswa yang memiliki **nilai semester 1 rendah**, **tidak membayar biaya kuliah tepat waktu**, atau **memiliki kebutuhan khusus**, menunjukkan kecenderungan lebih tinggi untuk dropout.
- Mahasiswa penerima **beasiswa** memiliki tingkat kelulusan lebih baik dibanding non-beasiswa.

### 🎯 Rekomendasi Action Items

Berikut beberapa langkah konkret yang disarankan untuk menurunkan angka dropout di Jaya Jaya Institute:
- Fokus pada jurusan dengan tingkat dropout tertinggi untuk peninjauan kurikulum atau dukungan belajar tambahan.
- Berikan perhatian lebih kepada siswa dengan nilai semester pertama rendah, karena berkorelasi dengan DO.
- Monitoring status *Debtor* dan *Tuition Not Up-to-Date* bisa menjadi indikator risiko DO.
- Pertimbangkan untuk memberi *intervensi awal* kepada siswa dengan usia pendaftaran lebih tinggi dari rata-rata.