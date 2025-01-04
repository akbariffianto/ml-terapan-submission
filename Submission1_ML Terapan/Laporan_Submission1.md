# Laporan Proyek Machine Learning - Nama Anda

## Domain Proyek

Industri real estat telah mengalami transformasi besar seiring dengan perkembangan teknologi analisis data. Pada masa lalu, penilaian dan pengambilan keputusan dalam real estat sering kali bergantung pada pengalaman subjektif, insting, atau informasi yang terbatas. Namun, pendekatan tradisional ini memiliki kelemahan signifikan, terutama dalam mengidentifikasi tren pasar yang tidak kentara dan memanfaatkan peluang investasi secara optimal. Kesalahan dalam menganalisis pasar atau menilai properti dapat menyebabkan kerugian besar, baik bagi investor maupun pemangku kepentingan lainnya.

Saat ini, analisis data telah menjadi alat penting yang dapat mengubah cara kita memahami pasar real estat. Dengan menggunakan data yang komprehensif, seperti tren historis, data waktu nyata, dan analisis geografis, investor dapat memperoleh wawasan yang lebih mendalam dan membuat keputusan yang lebih cerdas. Misalnya, analisis prediktif dapat memproyeksikan tren pasar masa depan, sementara alat visualisasi seperti peta panas dapat membantu dalam memahami pola dan risiko geografis. Dengan integrasi teknologi seperti kecerdasan buatan (AI) dan pembelajaran mesin, analisis data tidak hanya menjadi lebih cepat tetapi juga lebih akurat.

Masalah ini harus diselesaikan karena keterlambatan dalam mengidentifikasi peluang investasi yang dapat menyebabkan kerugian finansial besar. Analisis data memungkinkan pemangku kepentingan mendeteksi peluang lebih awal dan membuat langkah strategis. Selain itu, penilaian properti yang hanya mengandalkan faktor tradisional seperti lokasi, sering kali tidak mencerminkan nilai sebenarnya. Dengan analisis data, faktor-faktor seperti kondisi pasar lokal, properti komparatif, dan perkembangan masa depan dapat diperhitungkan, menghasilkan estimasi nilai yang lebih akurat. Analisis data juga membantu mengurangi risiko investasi, seperti volatilitas pasar dan tingkat kekosongan, dengan menyediakan wawasan tentang stabilitas pasar dan kondisi properti.
  
  Format Referensi: [Analisis Data Real Estat: Panduan bagi Para Pengambil Keputusan](https://predikdata.com/servicio/real-estate-data-and-analytics/)

## Business Understanding
### Problem Statements
- Bagaimana variabel seperti usia rumah, jarak ke stasiun MRT, dan jumlah toko di sekitar memengaruhi harga rumah per unit area?
- Apakah mungkin membangun model prediktif yang dapat memberikan estimasi harga rumah dengan akurasi yang baik berdasarkan fitur yang tersedia?

### Goals
Memahami hubungan antar variabel:
- Analisis hubungan antara fitur (usia rumah, jarak ke pusat kota, toko terdekat) dengan harga rumah per unit area.
- Identifikasi fitur-fitur yang paling signifikan dalam memengaruhi harga.
Mengembangkan model prediksi:
- Membuat model prediktif untuk memproyeksikan harga rumah berdasarkan dataset yang tersedia.
- Evaluasi model menggunakan metrik seperti Mean Squared Error (MSE).

### Solution Statement
Model Baseline:
- Menggunakan algoritma seperti K-Nearest Neighbors (KNN) dan Random Forest sebagai model dasar untuk prediksi harga rumah.
- Menggunakan algoritma Boosting (contohnya AdaBoostRegressor) untuk meningkatkan akurasi prediksi.
- Mengoptimalkan performa model melalui hyperparameter tuning.
- Menggunakan MSE pada data pelatihan dan pengujian untuk menilai performa masing-masing model.
- Membandingkan hasil prediksi dari beberapa model untuk memilih pendekatan terbaik.

## Data Understanding
Dataset yang digunakan merupakan data Real Estate yang dikumpulkan dari Sindian Dist., New Taipei City, Taiwan. Dataset terdiri dari 371 data dengan beberapa fitur yang digunakan untuk analisis dan pengembangan model prediksi harga rumah per unit area.
[Real Estate Valuation](https://archive.ics.uci.edu/dataset/477/real+estate+valuation+data+set).

Fitur Data
1. Variabel Diskrit:
  - Jumlah toko serba ada di sekitar properti (X4). Variabel ini telah diubah menjadi fitur dummy selama preprocessing.
2. Variabel Kontinu:
  - Tanggal Transaksi (X1): Direpresentasikan dalam format tahun desimal, mencerminkan waktu penjualan properti.
  - Usia Rumah (X2): Mengukur usia properti dalam tahun.
  - Jarak ke Stasiun MRT Terdekat (X3): Dalam satuan meter, digunakan untuk mengevaluasi aksesibilitas transportasi umum.
  - Lintang dan Bujur (X5, X6): Koordinat geografis properti.
3. Target Data: Harga Rumah per Unit Area (Y), Target variabel yang diukur dalam satuan moneter per meter persegi, 10000 New Taiwan Dollar/Ping, di mana Ping adalah satuan lokal, 1 Ping = 3,3 meter kuadrat



### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

