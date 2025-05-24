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

## 📊 Business Dashboard
**Akses dashboard online** : 

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
## 1. Faktor (Atribut) yang Paling Mempengaruhi Status Kelulusan

Dashboard menunjukkan bahwa faktor-faktor berikut sangat berpengaruh terhadap kelulusan mahasiswa:

- 🎓 **Beasiswa**: Mahasiswa penerima beasiswa memiliki tingkat kelulusan yang jauh lebih tinggi dibanding non-penerima.
- 📉 **Nilai Akademik**: Rata-rata nilai semester 1 & 2 yang rendah sangat berkorelasi dengan risiko dropout.
- 💰 **Status Keuangan**:
  - Mahasiswa dengan **tunggakan pembayaran** dan **biaya kuliah tidak lengkap** lebih banyak yang dropout.
- 👶 **Usia Saat Masuk**: Mahasiswa dengan usia terlalu muda atau terlalu tua cenderung memiliki risiko dropout lebih tinggi.

📌 **Kesimpulan**: Faktor dominan penyebab dropout adalah **nilai akademik rendah**, **tidak menerima beasiswa**, dan **masalah keuangan**.

---

## 2. Persentase Dropout dan Kelulusan Mahasiswa

| Status         | Jumlah | Persentase (%) |
|----------------|--------|----------------|
| Dropout        | 1421   | 32.12%         |
| Enrolled       | 794    | 17.96%         |
| Graduated      | 2209   | 49.95%         |
| **Total**      | 4424   | 100%           |

📌 **Kesimpulan**: Hampir **1 dari 3 mahasiswa mengalami dropout**, sementara **sekitar setengah berhasil lulus**.

---

## 3. Hubungan Status Beasiswa dengan Kelulusan

- Dari total penerima beasiswa:
  - ✅ 835 **lulus**
  - ❌ 134 **dropout**

📌 **Kesimpulan**: Mahasiswa penerima beasiswa memiliki **kemungkinan besar untuk lulus**, menunjukkan **dampak positif program beasiswa** dalam mencegah dropout.

---

## 4. Pengaruh Nilai Masuk terhadap Kelulusan

- Nilai masuk tinggi dan diikuti dengan performa baik di semester 1 & 2 → cenderung **lulus**
- Nilai masuk rendah + performa akademik anjlok → **dropout**

📌 **Kesimpulan**: **Nilai masuk** menjadi indikator awal yang penting, apalagi bila konsisten dengan performa awal kuliah.

---

## 5. Jurusan dengan Tingkat Dropout Tertinggi

Berikut adalah **Top 5 jurusan dengan dropout rate tertinggi**:

| Jurusan                             | Dropout Rate |
|------------------------------------|--------------|
| Biofuel Production Technologies     | 66.67%       |
| Equiniculture                       | 55.32%       |
| Informatics Engineering             | 51.21%       |
| Management (evening attendance)     | 50.71%       |
| Basic Education                     | 44.27%       |

📌 **Kesimpulan**: Jurusan-jurusan ini memerlukan **evaluasi kurikulum, dukungan tambahan, atau intervensi khusus** untuk menekan angka dropout.

---

## ✅ Kesimpulan Umum
Dashboard ini berhasil menjawab seluruh pertanyaan penelitian dengan **visualisasi data yang kuat dan actionable insight**, serta memberikan dasar pengambilan keputusan untuk **menekan angka dropout** di Jaya Jaya Institute.

### 🎯 Rekomendasi Action Items

Berikut beberapa langkah konkret yang disarankan untuk menurunkan angka dropout di Jaya Jaya Institute:
- Fokus pada jurusan dengan tingkat dropout tertinggi untuk peninjauan kurikulum atau dukungan belajar tambahan.
- Berikan perhatian lebih kepada siswa dengan nilai semester pertama rendah, karena berkorelasi dengan DO.
- Monitoring status *Debtor* dan *Tuition Not Up-to-Date* bisa menjadi indikator risiko DO.
- Pertimbangkan untuk memberi *intervensi awal* kepada siswa dengan usia pendaftaran lebih tinggi dari rata-rata.