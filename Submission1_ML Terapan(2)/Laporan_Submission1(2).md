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
Dataset yang digunakan merupakan data Real Estate yang dikumpulkan dari Sindian Dist., New Taipei City, Taiwan. Dataset terdiri dari 5519 data dengan beberapa fitur yang digunakan untuk analisis dan pengembangan model prediksi harga rumah per unit area.

Referensi: [Taiwan Taipei City Real Estate Transaction Records
](https://www.kaggle.com/datasets/chrischien17/taiwan-taipei-city-real-estate-transaction-records).

![Data Understanding](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/data_understanding.png?raw=true)
###### Dataset Preview 

## Exploratory Data Analysis

### Deskripsi Variabel:
Fitur Data
1. Kolom Kategorikal:
    - district = Distrik tempat transaksi real estat berlangsung (contoh: Daerah di Taipei seperti Xinyi, Wanhua, dll.).
    - transaction_type = Jenis transaksi yang dilakukan, misalnya pembelian, penjualan, sewa, atau lainnya.
    -urban_land_use = Penggunaan lahan perkotaan sesuai zonasi, seperti perumahan, komersial, atau industri.
    - main_use = Penggunaan utama bangunan atau properti, misalnya hunian, kantor, atau toko.
    - main_building_material = Jenis material utama yang digunakan untuk membangun properti, seperti beton, baja, atau kayu.
    - num_partition = Kategori yang menunjukkan jumlah sekat atau partisi di dalam properti (seperti open-space atau bersekat banyak).
    - management_org = Informasi tentang ada atau tidaknya organisasi pengelola properti (contoh: "yes" untuk properti yang dikelola oleh pihak ketiga, "no" untuk properti yang dikelola sendiri).
    - carpark_category = Kategori tempat parkir, seperti parkir di bawah tanah, parkir di luar ruangan, atau parkir tertutup.

2. Kolom Numerik:
    - land_shift_area = Luas lahan (dalam satuan tertentu, seperti meter persegi) yang termasuk dalam transaksi.
    - complete_year = Tahun penyelesaian konstruksi bangunan yang ditransaksikan.
    - building_shift_total_area = Total luas bangunan yang termasuk dalam transaksi (dalam meter persegi).
    - num_room = Jumlah kamar di dalam properti.
    - num_hall = Jumlah ruang tengah atau ruang serbaguna dalam properti.
    - num_toilet = Jumlah toilet atau kamar mandi di properti.
    - unit_ntd = Harga per satuan luas dalam mata uang NTD (contoh: NTD per meter persegi).
    - carpark_shift_area = Luas area tempat parkir yang termasuk dalam transaksi (dalam meter persegi).
    - carpark_ntd = Harga tempat parkir dalam mata uang NTD.
    - transaction_year = Tahun ketika transaksi berlangsung.
    - transaction_month = Bulan ketika transaksi berlangsung.
    - building_age = Usia bangunan (dalam tahun) pada saat transaksi dilakukan.
    - number_of_land = Jumlah bidang tanah yang termasuk dalam transaksi.
    - number_of_building = Jumlah bangunan yang termasuk dalam transaksi.
    - number_of_carpark = Jumlah tempat parkir yang termasuk dalam transaksi.

3. Fitur Target
    - total_ntd = Total harga transaksi dalam mata uang New Taiwan Dollar (NTD).


### Missing Value:
Dataset yang digunakan tidak memiliki data null atau kosong. Namun dalam dataset terdapat baris data dengan value 0.

![missing_value](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/missing_value.png?raw=true)

Terlihat dalam tabel kolom yang memiliki value 0 pada tabel diatas. Kolom data tersebut masuk akal memiliki value 0. Dikarenakan fitur data tersebut memiliki makna bahwa properti tidak memiliki fitur data tersebut. Seperti tidak memiliki kamar mandi, bangunan, dan lainnya. Namun karena terdapat value 0 pada kolom total_ntd dan unit_ntd yang menandakan bahwa total dan unit harga transaksi tidak ada dalam baris data yang memiliki nilai tersebut. Khusus untuk baris data yang memiliki value 0 pada kolom data total_ntd dan unit_ntd akan dihapus.

Dalam dataset yang digunakan memiliki baris data yang duplikat dan telah dihapus untuk mencegah hasil analisis yang tidak akurat.

### Menanggani Outlier:

![outlier](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/outlier.png?raw=true)

Dataset yang digunakan memiliki outlier di beberapa kolom fitur, outlier perlu diperhatikan dan dikelola dalam analisis data karena dapat memengaruhi hasil analisis, pemodelan, dan pengambilan keputusan. Namun tidak harus semua outlier harus dihapus. Oleh karena itu, sangat penting dalam memilih metode untuk menanggani outliers. 

#### Isolate forest method
Dalam proyek ini menggunakan metode isolate forest sebagai metode menanggani outlier dalam dataset yang digunakan.

Isolation Forest adalah metode yang unggul untuk deteksi outlier karena:
- Tidak bergantung pada asumsi distribusi data.
- Efisien secara komputasi, bahkan untuk dataset besar.
- Skalabel untuk data berdimensi tinggi dan kompleks.
- Lebih akurat dalam menangani dataset dengan kemiringan atau ekor berat dibandingkan metode klasik seperti Z-score atau IQR.
- Metode ini cocok untuk aplikasi dunia nyata yang melibatkan data besar, tidak terstruktur, atau memiliki distribusi yang kompleks.
```
from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(contamination=0.05, random_state=42)  # 5% dianggap outlier
outliers = iso_forest.fit_predict(realestate[numerical_features])
realestate_no_outliers = realestate[outliers == 1]

print(realestate_no_outliers.shape)
```
Reference: [Exploring Outlier Handling Techniques: A Comparative Analysis of Isolation Forest, Log-Transformation, and Random Forest on Paris Bike Count Data](https://medium.com/@hsu.lihsiang.esth/exploring-outlier-handling-techniques-a-comparative-analysis-of-isolation-forest-0b4836e215b8)
### Feature engineering:
Berdasarkan deskripsi data sebelumnya, terdapat fitur district atau tempat transaksi properti. Berdasarkan studi literatur yang digunakan, diketahui bahwa jarak dari pusta kota mempengaruhi nilai dari sebuh properti. Untuk mendapatkan fitur jarak dari pusat kota, sebagai hipotesis dikarenakan kolom fitur district merupakan kolom kategori dan memiliki 12 nilai atau district. Mungkin untuk mencari masing masing titik koordinat di tiap district. Dari titik koordinat tersbut akan dibandingkan dengan titik koordinat pusat kota dataset yaitu taipei dengan koordinat [Longitude= 121.5654, Latitude= 25.0320]

Metode Haversine cocok digunakan untuk mengukur jarak dari antar titik koordinat. 

Reference: [Quality of urban area, distance from city centre, and housing value. Case study on real estate values in Turin](https://www.sciencedirect.com/science/article/abs/pii/S0264275118308552)
``` 
def haversine(lat1, lon1, lat2, lon2):
    R = 6371 #Radius rata-rata bumi dalam kilometer
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)

    a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c
```
Haversine Formula:

Keterangan:
- sin^2(Δϕ/2): Menghitung kontribusi dari perbedaan latitude.
- cos(ϕ1)⋅cos(ϕ2): Menghitung faktor koreksi untuk longitude berdasarkan posisi latitude.
- sin^2(Δλ/2): Menghitung kontribusi dari perbedaan longitude.

Pada kolom management_org dan num_partition dataset menggunakan karakter Hanzi 有 (yǒu) yang berarti 'ada' dan 無 (wú) yang berarti 'tidak ada' untuk menandakan keberadaan atau ketiadaan value pada kolomnya. Agar dalam menganalisis dan memodelkan dataset di langkah akhir, keputusan mengubah karakter tersebut menjadi 1 dan 0 disarankan untuk dilakukan. 

### Univariate Analysis:
![Univariate](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/univariate.png?raw=true)

#### Categorical Features: 

![district](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/district.png?raw=true)

**district**: 
Distrik Zhongshan memiliki persentase paling tinggi dalam fitur district. Zhongshan sendiri merupakan kota yang paling sibuk di kota taipei, jadi masuk akal jika distrik ini memilik persentasi paling tinggi. Namun urutan data distrik ini bukan berdasarkan penduduk terbesar maupun daerah terluas.

![transaction_type](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/transaction_type.png?raw=true)

**transaction_type**: Distribusi tipe transaksi dalam dataset properti menunjukkan bahwa mayoritas transaksi (60%, 3336 sampel) didominasi oleh tipe "Premises (Tanah & Bangunan)", yang mengindikasikan bahwa sebagian besar transaksi melibatkan penjualan atau pembelian properti yang sudah berdiri di atas tanah. Tipe transaksi "Premises + Parkir (Tanah & Bangunan + Tempat Parkir)" juga cukup signifikan, mencakup 27% (1485 sampel) dari total transaksi, yang menyoroti pentingnya ketersediaan tempat parkir dalam pasar properti. Sebaliknya, transaksi yang hanya melibatkan "Tanah (Land)" relatif sedikit, yaitu 8% (436 sampel), menunjukkan bahwa transaksi tanah kosong lebih jarang terjadi. Hal serupa juga terlihat pada transaksi "Garasi (Garage)" yang hanya mencakup 4% (239 sampel), mengindikasikan bahwa transaksi garasi terpisah juga tidak umum. Terakhir, transaksi yang hanya melibatkan "Bangunan (Building)" sangat jarang, kurang dari 1% (hanya 23 sampel), kemungkinan besar karena secara hukum dan praktis, kepemilikan bangunan seringkali terkait erat dengan tanah tempat bangunan tersebut berdiri.

![urban_land_use](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/urban_land_use.png?raw=true)

**urban_land_use**: Dataset didominasi oleh penggunaan lahan untuk "Address" (Alamat/Perumahan) (60%), diikuti oleh "Quotient" (kemungkinan area komersial/campuran) (28%). Penggunaan lahan untuk "Other" (Lainnya) cukup signifikan (10%), sementara "work" (kerja), "Others" (Lain-lain), dan "Agriculture" (Pertanian) sangat sedikit (<1%). Dataset ini cenderung berfokus pada properti residensial dan kemungkinan area komersial/campuran.

![main_use](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/main_use.png?raw=true)

**main_use**: Penggunaan utama properti didominasi oleh "Resident" (Hunian) dengan 64.7% (3572 sampel). Diikuti oleh "See other registration items" (Lihat item registrasi lainnya) dengan 22.6% (1246 sampel), yang memerlukan penjelasan lebih lanjut mengenai isi kategori ini. Penggunaan "For commercial use" (Untuk penggunaan komersial) sebesar 7.9% (436 sampel) cukup signifikan. Kategori-kategori lain seperti "See license" (Lihat lisensi), "Parking space" (Tempat parkir), "Residential business" (Bisnis hunian), "industrial use" (Penggunaan industri), dan "For work" (Untuk pekerjaan) memiliki persentase yang sangat kecil (<2.5% masing-masing). Dataset ini menunjukkan fokus utama pada properti hunian, dengan sebagian kecil untuk penggunaan komersial dan kategori lainnya.

![main_building_material](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/main_building_material.png?raw=true)

**main_building_material**: Sebagian besar properti (81.2%) dibangun dengan konstruksi beton bertulang ("Reinforced concrete construction"). Kategori "Not Applicable" (Tidak Berlaku) menempati urutan kedua (8.9%), yang perlu investigasi lebih lanjut. Bahan lain seperti "Strengthen brickwork" (Dinding bata yang diperkuat) (4.5%), "See other registration items" (Lihat item registrasi lainnya) (2.6%), dan "Steel reinforced concrete construction" (Konstruksi beton bertulang baja) (2.0%) muncul dalam jumlah kecil. Bahan-bahan lain sangat jarang (<0.5%). 

![num_partition](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/num_partition.png?raw=true)

**num_partition**: Data fitur `num_partition` menunjukkan ketidakseimbangan yang sangat signifikan. Sebagian besar data (93.6% atau 5166 sampel) berada dalam kategori "1", sementara hanya sebagian kecil (6.4% atau 353 sampel) berada dalam kategori "0". Singkatnya, hampir semua sampel memiliki nilai "1" pada fitur num_partition, sehingga fitur ini mungkin kurang informatif atau bahkan tidak berguna untuk beberapa jenis analisis atau pemodelan karena kurangnya variasi.

![management_org](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/management_org.png?raw=true)

**management_org**: Distribusi fitur management_org menunjukkan bahwa mayoritas sampel (57% atau 3146 sampel) memiliki nilai "1", sedangkan sisanya (43% atau 2373 sampel) memiliki nilai "0". Meskipun terdapat perbedaan jumlah antara kedua kategori, perbedaannya tidak terlalu besar dan kedua kategori terwakili dengan cukup baik. Singkatnya, fitur management_org menunjukkan distribusi yang cukup seimbang antara dua kategori, meskipun kategori "1" sedikit lebih dominan.

#### Numerical Features:

![numeric_univariate](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/numeric_univariate.png?raw=true)

Jika dilihat dari grafik distribusi seluruh fitur numerik, dapat ditarik beberapa kesimpulan:
- Tidak banyak dari semua fitur peningkatan nilai fitur tidak sebanding dengan penurunan jumlah sampel
- `land_shift_area` dan `building_shift_total_area`: Terlihat sangat miring ke kanan (positively skewed). Sebagian besar properti memiliki luas yang relatif kecil, dengan beberapa properti yang memiliki luas yang sangat besar, menarik distribusi ke arah kanan.
- `total_ntd` dan `unit_ntd`: Juga miring ke kanan, meskipun mungkin tidak separah dua fitur sebelumnya. Ini menunjukkan bahwa sebagian besar properti memiliki nilai NTD (New Taiwan Dollar).
- `building_age`: Tampaknya memiliki dua puncak (bimodal), mungkin menunjukkan dua periode konstruksi yang berbeda atau dua jenis properti yang berbeda. Pada periode 2020 terjadi penurunan yang ekstrim. 
- `distance_from_city_center` : Juga terlihat bimodal, mungkin mencerminkan konsentrasi properti di sekitar pusat kota dan di daerah yang lebih jauh.

### Multivariate Analysis

#### Categorical Features:

![categorical_multi](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/categorical_multi.png?raw=true)

- Properti dengan material `Stone building` memiliki rata-rata nilai tertinggi, yang mengindikasikan bahwa properti yang dibangun dengan batu cenderung lebih mahal.
- Beberapa kategori memiliki rata-rata nilai yang relatif rendah: Kategori seperti `Wooden` (Kayu), `Earthen masonry` (Batu bata tanah), dan `Wall type reinforced concrete construction` (Konstruksi dinding beton bertulang) menunjukkan rata-rata total_ntd yang lebih rendah. Ini mungkin mengindikasikan bahwa bahan-bahan ini digunakan untuk properti yang lebih sederhana atau lebih tua.
- Variasi dalam setiap kategori: Garis vertikal pada setiap bar menunjukkan variasi (kemungkinan standar deviasi atau interval kepercayaan) dalam `total_ntd` untuk setiap kategori `main_building_material`. Beberapa kategori, seperti `See other registration items` (Lihat item registrasi lainnya) dan `Steel reinforced concrete construction` (Konstruksi beton bertulang baja), menunjukkan variasi yang cukup besar, yang berarti nilai properti dalam kategori ini sangat bervariasi.

**Numerical Features**
Hubungan fitur numerik dengan fitur target dapat diukur dengan menggunakan metode spearman. Spearman mengukur korelasi monotonik, yang berarti mengukur apakah hubungan antara dua variabel cenderung bergerak bersama, tetapi tidak harus dalam garis lurus. Ini berguna karena data properti seringkali tidak mengikuti hubungan linier yang sempurna. Jadi metode spearman cukup menjadi pilihan yang direkomendasikan apabila fitur numerik berifat non-linear terhadap fitur target.

![heatmap](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/heatmap.png?raw=true)

Dari heatmap dapat diambil beberapa informasi: 
- `building_shift_total_area` (0.82): Ini adalah korelasi positif terkuat dengan total_ntd. Ini sangat logis: semakin besar luas bangunan, semakin tinggi pula nilai propertinya. Hubungan ini sangat penting dan kemungkinan besar akan menjadi prediktor yang kuat dalam model prediksi harga.
- `num_room` (0.44), `num_hall` (0.45), `num_toilet` (0.49): Jumlah kamar, ruang tengah, dan toilet semuanya berkorelasi positif sedang dengan `total_ntd`. Ini juga masuk akal, karena properti dengan lebih banyak kamar dan fasilitas cenderung lebih mahal.
- `carpark_ntd` (0.41): Nilai tempat parkir juga berkorelasi positif sedang dengan `total_ntd`. Ini menunjukkan bahwa tempat parkir berkontribusi pada nilai total properti.
- `building_age` (-0.41): Usia bangunan berkorelasi negatif sedang dengan `total_ntd`. Properti yang lebih tua cenderung memiliki nilai yang lebih rendah.


## Data Preparation
### Encoding Fitur Kategori: 
One Hot Encoding adalah teknik yang digunakan untuk mengonversi variabel kategorikal menjadi format numerik agar dapat digunakan dalam algoritma machine learning. Proses ini penting karena mayoritas algoritma machine learning hanya dapat memproses data dalam bentuk numerik. Dengan bantuan library Pandas, proses ini dapat dilakukan dengan mudah menggunakan fungsi pd.get_dummies(). Fungsi tersebut secara otomatis membuat kolom baru untuk setiap nilai unik dalam variabel kategorikal. Pada setiap baris, kolom yang sesuai dengan nilai tertentu akan diberi nilai 1, sementara kolom lainnya diatur menjadi 0.

### Splitting data
Di projek ini, proporsi pembagian data yang digunakan adalah `80:20` dikarenakan ukuran dataset sedang dan tidak ada ketidakseimbangan data yang parah dan ukuran datasetnya yang cukup banyak (>5000).

### Standarisasi Fitur
Proses standarisasi dilakukan untuk memudahkan algoritma machine learning menjadi bentuk yang lebih mudah diolah. Standardisasi adalah teknik transformasi yang paling umum digunakan dalam tahap persiapan pemodelan. Seperti fitur kategori menggunakan one-hot-encoding, fitur numerik menggunakan teknik `StandarScaler` dari library scikitlearn. Proses standarisasi fitur dilakukan dengan mengurangi nilai rata-rata (mean) dari setiap fitur dan membaginya dengan standar deviasi. Langkah ini bertujuan untuk menggeser distribusi data sehingga memiliki nilai rata-rata 0 dan standar deviasi 1. Dengan menggunakan StandardScaler, distribusi data menjadi memiliki standar deviasi sebesar 1 dan rata-rata 0, sehingga sekitar 68% nilai data berada di rentang -1 hingga 1.

### Reduksi dimensi fitur dengan PCA
Reduksi dimensi adalah metode untuk mengurangi jumlah fitur dalam dataset sambil tetap mempertahankan informasi penting. Salah satu teknik reduksi dimensi yang paling umum digunakan adalah Principal Component Analysis (PCA). PCA adalah metode yang digunakan untuk mengurangi dimensi data, mengekstrak fitur, dan mentransformasikan data dari ruang berdimensi n ke dalam sistem koordinat baru dengan dimensi m, di mana m lebih kecil dari n.

PCA bekerja dengan memanfaatkan konsep aljabar linier dan mengidentifikasi arah dengan varians terbesar dalam data, karena arah tersebut dianggap paling signifikan. Teknik ini sangat berguna ketika variabel dalam dataset memiliki korelasi yang tinggi, yang menunjukkan adanya redundansi atau pengulangan informasi dalam data.

Berikut grafik pairplot untuk melihat skor korelasi fitur numerik untuk menggabungkannya sehingga data yang digunakan dimensinya(fitur) berkurang.
![Facility PCA](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/facility_pca.png?raw=true)

###### Korelasi PCA

Mereduksi dimensi sebuah data tidak hanya dilihat dari korelasi dari pairplot yang digunakan. Penting untuk mengetahui proporsi informasi dari hasil penggabungan fitur numerik. Berikut kode untuk mencari tahu informasi tersebut:
```
pca.explained_variance_ratio_.round(3)
```
Berikut output masing-masing operasi PCA yang dilakukan dalam projek ini:
- building_age dan complete_year

    `array([1., 0.])`
    
    kedua fitur ini memiliki skor korelasi yang sempurna, jadi langkah yang diambil adalah bebas menghapus salah satu fitur. Fitur yang dihapus dalam projek ini adalah building_age.
- carpark_shift_area dan carpark_ntd

    `array([0.83, 0.17])`
    
    kedua fitur ini memiliki skor korelasi yang tinggi (>60), jadi langkah yang diambil adalah menggabungkan kedua informasi tersebut dengan menggunakan proporsi pertama. Kolom baru ditambahkan dengan nama `carpark_area_ntd` yang menampung nilai PCA antara 2 fitur tersebut.
- num_hall, num_room, dan num_toilet

    `array([0.829, 0.119, 0.051])`
    
    ketiga fitur ini memiliki skor korelasi yang tinggi (>60), jadi langkah yang diambil adalah menggabungkan ketiga informasi tersebut dengan menggunakan proporsi pertama. Kolom baru ditambahkan dengan nama `facility` yang menampung nilai PCA antara 3 fitur tersebut.

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

![Setelah Hypertuning](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/setelah_hypertuning.png?raw=true)

Dari grafik di atas, terlihat bahwa, model Random Forest (RF) memberikan nilai eror yang paling kecil. Sedangkan model dengan algoritma Boosting memiliki eror yang paling besar. Sehingga model RF yang akan dipilih sebagai model terbaik untuk melakukan prediksi harga properti.

### Proses Hyperparameter Tuning
Hyperparameter tuning dilakukan pada model yang digunakan untuk meningkatkan performa model. 

**Pendekatan**:
Menggunakan pencarian grid (GridSearchCV) untuk menemukan kombinasi parameter terbaik berdasarkan skor Mean Squared Error (MSE) pada validasi silang. Mengoptimalkan hyperparameter menggunakan GridSearchCV.

### Hasil Evaluasi Setelah Hyperparameter Tuning
Hasil evaluasi pada data latih dan data test adalah sebagai berikut.

![Sebelum Hypertuning](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission1_ML%20Terapan(2)/assets/sebelum_hypertuning.png?raw=true)

Berdasarkan nilai MSE, model Random Forest (RF) adalah pilihan terbaik untuk dataset ini. RF memberikan prediksi yang paling akurat dengan potensi overfitting yang paling kecil dibandingkan KNN dan Boosting. Meskipun Boosting memberikan performa yang lebih baik dari KNN, ia masih menunjukkan potensi overfitting yang lebih tinggi dibandingkan RF. Perlu diingat bahwa ini hanya berdasarkan metrik MSE. Evaluasi metrik lain seperti R-squared, MAE, atau RMSE juga disarankan untuk mendapatkan gambaran yang lebih komprehensif. Selain itu, teknik cross-validation dapat digunakan untuk validasi yang lebih kuat.

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
