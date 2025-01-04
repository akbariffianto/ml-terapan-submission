# Laporan Proyek Machine Learning - Akbar Ariffianto
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

Referensi: [Real Estate Valuation](https://archive.ics.uci.edu/dataset/477/real+estate+valuation+data+set).

![Data Understanding](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan/assets/Data%20Understanding.png?raw=true)
###### Dataset Preview 

## Exploratory Data Analysis

### Deskripsi Variabel:
Fitur Data
1. Variabel Diskrit:
    - Jumlah toko serba ada di sekitar properti (X4).
2. Variabel Kontinu:
    - Tanggal Transaksi (X1): Direpresentasikan dalam format tahun desimal, mencerminkan waktu penjualan properti.
    - Usia Rumah (X2): Mengukur usia properti dalam tahun.
    - Jarak ke Stasiun MRT Terdekat (X3): Dalam satuan meter, digunakan untuk mengevaluasi aksesibilitas transportasi umum.
    - Lintang dan Bujur (X5, X6): Koordinat geografis properti.
3. Fitur Target: Harga Rumah per Unit Area (Y), Target variabel yang diukur dalam satuan moneter per meter persegi, 10000 New Taiwan Dollar/Ping, di mana Ping adalah satuan lokal, 1 Ping = 3,3 meter kuadrat.

### Missing Value:
Dataset yang digunakan tidak memiliki data null atauk kosong maupun data yang valuenya duplikat. Namun dalam dataset terdapat baris data dengan value 0.

Terlihat dalam tabel kolom yang memiliki value 0 adalah X2(Umur Rumah) dan X4(Jumlah Toko Swalayan). Kolom data ini masuk akal memiliki data dengan value 0. X2 memiliki data 0 berindikasikan bahwa rumah tersebut baru atau belum berumur 1 tahun. Sedangkan unruk X4 memiliki data dengan value 0, menyatakan kalau di dekat properti tersebut memiliki toko swalayan.

Untuk kolom 'No' atau nomor dari tiap baris data dihapus karena tidak memiliki hubungan yang relevan dalam membangun model nantinya.

### Menanggani Outlier:
Dataset yang digunakan memiliki outlier di beberapa kolom fitur, metode yang dipilih untuk menangganinya, projek ini menggunakan IQR sebagai metode yang digunakan untuk menanggani outlier. IQR adalah singkatan dari Inter Quartile Range. Sesuai namanya, menghitung rentang antara Q1 dan Q3, yang pada dasarnya memberi gambaran tentang distribusi data dan seperti yang dilihat di visualisasi data lewat boxplot seperti berikut. 
![Outlier](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan/assets/outlier.png?raw=true)
###### Outlier

IQR memungkinkan menentukan ambang batas bawah dan atas untuk nilai yang dapat diterima berdasarkan data yang digunakan.


### Feature engineering:
Berdasarkan deskripsi data sebelumnya, kolom data X5 dan X6 merupakan kolom yang memiliki value koordinat bumi yaitu bujur dan lintang. Dari informasi ini penggunaan metode haversine untuk mendapatkan jarak dari koordinat yang ditentukan ke koordinat lainnya. Di projek ini titik koordinat yang digunakan adalah Sindian Dist., New Taipei City, Taiwan yaitu [121.5398, 24.9785]. Dari informasi inilah *Jarak dari pusat kota* dapat ditambahkan sebagai fitur baru. 

``` 
from sklearn.metrics.pairwise import haversine_distances

pusat_kota = [121.5398, 24.9785]  # Sindian Dist., New Taipei City
kordinat = realestate[['x6', 'x5']].values  # Kolom x6 (longitude), x5 (latitude)

# Konversi ke radian
kordinat_radians = np.radians(kordinat)
pusat_kota_radians = np.radians(pusat_kota)

# Hitung jarak Haversine
jarak = haversine_distances(kordinat_radians, pusat_kota_radians.reshape(1, -1))

# Konversi ke kilometer (radius bumi = 6371 km)
jarak_km = jarak * 6371
realestate['jarak_ke_pusat(km)'] = jarak_km

print(realestate[['x5', 'x6', 'jarak_ke_pusat(km)']].head())
```

### Univariate engineering:
![Univariate](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan/assets/univariate.png?raw=true)
###### Univariate
**Categorical Features**: Terdapat 11 kategori pada kolom fitur data X4(Jumlah Toko Swalayan terdekat). Dapat disimpulkan kategori dengan value 5 umum dalam dataset yang digunakan.

**Numerical Features**:
1. Fitur x1 (Tahun dan Bulan):
    - Data pada x1 merepresentasikan waktu (mungkin dalam bentuk tahun dan bulan), dengan rentang waktu dari 2012.8 hingga 2013.6.
    - Distribusi terlihat cukup merata, tanpa adanya tren kenaikan atau penurunan jumlah sampel yang signifikan di periode tertentu.
    - Informasi ini menunjukkan bahwa data dikumpulkan secara konsisten selama periode waktu tersebut.

2. Fitur x2
    - Distribusi x2 menunjukkan pola bimodal, dengan puncak utama di sekitar 10 dan 20-30.
    - Rentang nilai yang tinggi di fitur ini mungkin mencerminkan variasi besar dalam karakteristik yang diukur, seperti ukuran atau atribut properti.
    - Kelompok data yang berada di sekitar kedua puncak dapat menunjukkan adanya segmentasi dalam data, misalnya properti di dua lokasi atau tipe yang berbeda.

3. Fitur x3 (Jarak ke Stasiun MRT)
    - Histogram x3 sangat miring ke kanan (right-skewed). Sebagian besar properti berada di dekat stasiun MRT, dengan jarak di bawah 500 meter.
    - Rentang jarak sangat luas, hingga lebih dari 3000 meter, namun hanya sedikit properti yang berada jauh dari stasiun MRT.
    - Informasi ini menunjukkan pentingnya lokasi dalam data properti. Properti yang lebih dekat ke stasiun MRT kemungkinan lebih diminati atau bernilai lebih tinggi.

4. Fitur x4 (Kategori)
    - Fitur kategori x4 menunjukkan bahwa kategori 5 memiliki jumlah sampel tertinggi, diikuti oleh kategori 3 dan 6.
    - Beberapa kategori seperti 10 hanya memiliki sedikit sampel, yang mungkin membutuhkan perhatian khusus saat digunakan dalam analisis, terutama untuk menghindari bias dalam model.

5. Fitur y (Target)
    - Histogram y menunjukkan pola yang mendekati distribusi normal, dengan sedikit kemiringan ke kanan (right-skewed).
    - Sebagian besar properti memiliki nilai target (kemungkinan harga) di sekitar 40, dengan beberapa nilai ekstrim di bagian atas dan bawah distribusi.
    - Properti dengan nilai yang sangat tinggi atau rendah mungkin perlu dianalisis lebih dalam untuk mengidentifikasi faktor-faktor yang memengaruhinya.

6. Fitur jarak_ke_pusat(km)
    - Distribusi fitur ini juga sangat miring ke kanan (right-skewed), mirip dengan x3. Sebagian besar properti terletak di bawah 1.5 km dari pusat kota.
    - Properti yang berada lebih jauh dari pusat kota mungkin mewakili wilayah suburban atau rural, yang dapat memiliki karakteristik berbeda dibandingkan properti yang lebih dekat.

### Multivariate Analysis
![Heatmap](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan/assets/Heatmap.png?raw=true)
###### Heatmap

**Categorical Features**: Kolom fitur data X4, memiliki pengaruh atau dampak dimana semakin banyak toko swalayan terdekat maka nilai jual dari properti juga naik

**Numerical Features**: Pada pola sebaran data grafik pairplot berikut, bisa disimpulkan Fitur dengan Pengaruh Kuat adalah :
- X3 (Jarak ke MRT) dan jarak_ke_pusat(km) adalah fitur dengan pengaruh negatif yang kuat terhadap nilai target y. Kedekatan ke MRT dan pusat kota meningkatkan nilai properti.
- X2 (Usia Bangunan) juga memengaruhi nilai properti secara signifikan, dengan properti yang lebih baru memiliki nilai lebih tinggi.
Fitur dengan Pengaruh Lemah:
- jarak_ke_pusat (Jarak properti ke pusat kota) mempengaruhi nilai properti dengan negatif dimana semakin dekat dengan pusat kota maka semakin tinggi nilai properti

Fitur dengan pengaruh lemah:
- X1 (Tanggal Transaksi) tampaknya tidak memiliki hubungan yang signifikan dengan nilai properti.

### Hubungan korelasi antar fitur
Projek ini menggunakan metode spearman dalam mencari skor korelasi antar fitur.Fitur X2, X3, X4, dan jarak_ke_pusat memiliki skor korelasi yang besar dibandingan dengan fitur X1. Sehingga fitur X1 akan di drop.
`realestate.drop(['x1'], inplace=True, axis=1)`

## Data Preparation
### Encoding Fitur Kategori: 
One Hot Encoding adalah teknik yang digunakan untuk mengonversi variabel kategorikal menjadi format numerik agar dapat digunakan dalam algoritma machine learning. Proses ini penting karena mayoritas algoritma machine learning hanya dapat memproses data dalam bentuk numerik. Dengan bantuan library Pandas, proses ini dapat dilakukan dengan mudah menggunakan fungsi pd.get_dummies(). Fungsi tersebut secara otomatis membuat kolom baru untuk setiap nilai unik dalam variabel kategorikal. Pada setiap baris, kolom yang sesuai dengan nilai tertentu akan diberi nilai 1, sementara kolom lainnya diatur menjadi 0.
```
from sklearn.preprocessing import  OneHotEncoder
realestate = pd.concat([realestate, pd.get_dummies(realestate['x4'], prefix='x4').astype(int)], axis=1)
realestate.drop(['x4'], axis=1, inplace=True)
realestate.head()
```

### Splitting data
Di projek ini, proporsi pembagian data yang digunakan adalah `70:30` dikarenakan ukuran dataset sedang dan tidak ada ketidakseimbangan data yang parah.

### Standarisasi Fitur
Proses standarisasi dilakukan untuk memudahkan algoritma machine learning menjadi bentuk yang lebih mudah diolah. Standardisasi adalah teknik transformasi yang paling umum digunakan dalam tahap persiapan pemodelan. Seperti fitur kategori menggunakan one-hot-encoding, fitur numerik menggunakan teknik `StandarScaler` dari library scikitlearn. Proses standarisasi fitur dilakukan dengan mengurangi nilai rata-rata (mean) dari setiap fitur dan membaginya dengan standar deviasi. Langkah ini bertujuan untuk menggeser distribusi data sehingga memiliki nilai rata-rata 0 dan standar deviasi 1. Dengan menggunakan StandardScaler, distribusi data menjadi memiliki standar deviasi sebesar 1 dan rata-rata 0, sehingga sekitar 68% nilai data berada di rentang -1 hingga 1.

### Reduksi dimensi fitur dengan PCA
Reduksi dimensi adalah metode untuk mengurangi jumlah fitur dalam dataset sambil tetap mempertahankan informasi penting. Salah satu teknik reduksi dimensi yang paling umum digunakan adalah Principal Component Analysis (PCA). PCA adalah metode yang digunakan untuk mengurangi dimensi data, mengekstrak fitur, dan mentransformasikan data dari ruang berdimensi n ke dalam sistem koordinat baru dengan dimensi m, di mana m lebih kecil dari n.

PCA bekerja dengan memanfaatkan konsep aljabar linier dan mengidentifikasi arah dengan varians terbesar dalam data, karena arah tersebut dianggap paling signifikan. Teknik ini sangat berguna ketika variabel dalam dataset memiliki korelasi yang tinggi, yang menunjukkan adanya redundansi atau pengulangan informasi dalam data.

Berikut grafik pairplot untuk melihat skor korelasi seluruh fitur numerik yang digunakan.
![Korelasi PCA](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan/assets/Korelasi%20PCA.png?raw=true)
###### Korelasi PCA

Terlihat bahwa fitur X3(Jarak ke MRT) dengan jarak_ke_pusat memiliki korelasi yang tinggi maka kedua fitur ini akan direduksi dimensinya menjadi fitur baru dengan nama kolom fiturnya 'jarak MRT ke pusat kota'.

## Modeling
Tahapan ini berfokus pada pengembangan model machine learning untuk menyelesaikan permasalahan prediksi harga properti (variabel target y). Pada tahap ini, digunakan dua algoritma machine learning, yaitu Linear Regression dan Random Forest Regressor, untuk membandingkan performa masing-masing model. Berikut adalah rincian proses pemodelan:

### Algoritma yang Digunakan
#### K-Nearest Neighbor
Dengan singkatan KNN, K-nearest neighbor merupakan algoritma yang digunakan untuk mengidentifikasi adanya persamaan antara data baru dan lama. Kemudian, data baru akan diinput dalam kategori yang paling mirip dengan kategori yang telah ada sebelumnya. Dengan kata lain, K-nearest neighbor menyimpan seluruh data lama dan mengklasifikasikan data point baru berdasarkan kemiripan.

```
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor(n_neighbors=15)
knn.fit(X_train, y_train)

models.loc['train_mse','KNN'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)
```
Projek ini menggunakan `n_neighbors=15` dan metric Euclidean untuk mengukur jarak antara titik.

#### Random Forest Regressor
Random forest adalah sebuah model machine learning yang digunakan untuk tugas klasifikasi dan regresi. Algoritma ini merupakan bentuk ensemble learning, yang berarti menggabungkan beberapa model prediktif yang lebih sederhana untuk mencapai prediksi yang lebih akurat dan stabil.

```
from sklearn.ensemble import RandomForestRegressor

RF = RandomForestRegressor(n_estimators=20, max_depth=5, random_state=35, n_jobs=-1)
RF.fit(X_train, y_train)

models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)
```

Parameter yang digunakan:
- n_estimator: jumlah trees (pohon) di forest.
- max_depth: kedalaman atau panjang pohon. Ia merupakan ukuran seberapa banyak pohon dapat membelah (splitting) untuk membagi setiap node ke dalam jumlah pengamatan yang diinginkan.
- random_state: digunakan untuk mengontrol random number generator yang digunakan. 
- n_jobs: jumlah job (pekerjaan) yang digunakan secara paralel. Ia merupakan komponen untuk mengontrol thread atau proses yang berjalan secara paralel. n_jobs=-1 artinya semua proses berjalan secara paralel.

#### Boosting Algorithm: Adaptive Boosting
Algoritma yang menggunakan teknik boosting bekerja dengan membangun model dari data latih. Kemudian ia membuat model kedua yang bertugas memperbaiki kesalahan dari model pertama. Model ditambahkan sampai data latih terprediksi dengan baik atau telah mencapai jumlah maksimum model untuk ditambahkan. Singkatnya, kita dapat mengatakan bahwa adaptive boosting adalah cara untuk mengurangi kesalahan algoritma machine-learning, yang bekerja dengan menyelaraskan banyak model machine-learning yang lemah mejadi satu model machine-learning yang kuat.

```
from sklearn.ensemble import AdaBoostRegressor

boosting = AdaBoostRegressor(n_estimators=300,
                             learning_rate=0.01,
                             random_state=42)

boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)
```
Parameter yang digunakan:
- learning_rate: bobot yang diterapkan pada setiap regressor di masing-masing proses iterasi boosting.
- random_state: digunakan untuk mengontrol random number generator yang digunakan.

## Evaluation
### Metrik yang digunakan
Model regresi dikenal relatif sederhana. Metrik yang akan digunakan pada prediksi ini adalah MSE atau Mean Squared Error yang menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi. MSE didefinisikan dalam persamaan berikut.

Keterangan:

![mse](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan/assets/mse.jpeg?raw=true)
- N = jumlah dataset
- yi = nilai sebenarnya
- y_pred = nilai prediksi

Fungsi kuadrat dalam MSE memiliki sifat matematika yang baik, yaitu dapat diturunkan secara matematis. Hal ini penting dalam optimasi model regresi, di mana mencari parameter model yang meminimalkan MSE sering dilakukan. Kemudahan dalam penurunan matematis ini memfasilitasi penggunaan algoritma optimasi seperti gradient descent.

### Hasil Evaluasi Sebelum Hyperparameter Tuning
Hasil evaluasi pada data latih dan data test adalah sebagai berikut.
![Sebelum tuning](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan/assets/Sebelum%20tuning.png?raw=true)
Dari grafik di atas, terlihat bahwa, model Random Forest (RF) memberikan nilai eror yang paling kecil. Sedangkan model dengan algoritma Boosting memiliki eror yang paling besar. Sehingga model RF yang akan dipilih sebagai model terbaik untuk melakukan prediksi harga properti.

### Proses Hyperparameter Tuning
Hyperparameter tuning dilakukan pada model yang digunakan untuk meningkatkan performa model. 

**Pendekatan**:
Menggunakan pencarian grid (GridSearchCV) untuk menemukan kombinasi parameter terbaik berdasarkan skor Mean Squared Error (MSE) pada validasi silang. Mengoptimalkan hyperparameter menggunakan GridSearchCV.

### Hasil Evaluasi Setelah Hyperparameter Tuning
Hasil evaluasi pada data latih dan data test adalah sebagai berikut.
![Setelah tuning](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan/assets/setelah%20tuning.png?raw=true)
Memiliki nilai MSE training dan testing terendah di antara ketiga model. Ini menunjukkan bahwa RF memberikan prediksi terbaik, baik pada data training maupun data testing. Selisih antara MSE training dan testing juga relatif kecil, menandakan model ini memiliki generalisasi yang baik dan tidak cenderung overfitting.

## Kesimpulan
Proyek ini berhasil mengembangkan model analisis prediktif menggunakan model Random Forest yang mampu memperkirakan harga real estate berdasarkan jumlah toko swalayan terdekat, jarak ke MRT, dan akses MRT ke pusat kota dengan tingkat akurasi yang lebih tinggi.

Hasil evaluasi menunjukkan bahwa model Random Forest memberikan MSE pada data training dan test set, serta evaluasi score yang lebih baik pada data testing. Hal ini menunjukkan bahwa model dapat memberikan prediksi harga real estate yang lebih akurat dan bermanfaat bagi pengembang properti, investor, pembeli rumah.

Manfaat bagi Pihak yang berhubungan dengan pemilikian properti:
- Harga yang lebih transparan dan adil: Model dapat memberikan estimasi harga yang lebih objektif berdasarkan faktor-faktor yang relevan, sehingga pembeli dapat memiliki referensi yang lebih baik dalam proses negosiasi harga.
- Pemahaman yang lebih baik tentang nilai properti: Dengan memahami faktor-faktor yang mempengaruhi harga, pembeli dapat membuat keputusan pembelian yang lebih informed dan sesuai dengan kebutuhan dan anggaran mereka.

Dengan mengambil keputusan ini, kepemilikan properti dapat memanfaatkan model analisis prediktif ini untuk meningkatkan ketepatan penentuan harga, pengambilan keputusan investasi, dan memberikan manfaat yang lebih baik bagi semua pihak yang terlibat dalam transaksi real estate.

## Reference
Referensi: 
- [Understanding the AdaBoost Algorithm](https://medium.com/@datasciencewizards/understanding-the-adaboost-algorithm-2e9344d83d9b).
- [Serba Serbi Machine Learning Model Random Forest
](https://dqlab.id/serba-serbi-machine-learning-model-random-forest)
