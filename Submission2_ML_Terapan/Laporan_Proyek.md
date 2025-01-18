# Laporan Proyek Machine Learning - Akbar Ariffianto

## 1. Project Overview

Sistem rekomendasi sangat penting dalam dunia digital saat ini, di mana pengguna sering kali dihadapkan pada informasi yang berlebihan. Dengan banyaknya pilihan produk, layanan, atau konten yang tersedia, sistem rekomendasi membantu menyaring informasi dan memberikan saran yang relevan serta dipersonalisasi berdasarkan preferensi dan perilaku pengguna sebelumnya. Hal ini tidak hanya meningkatkan pengalaman pengguna, tetapi juga dapat meningkatkan kepuasan pelanggan dan loyalitas terhadap merek. Menurut penelitian, personalisasi yang diberikan oleh sistem rekomendasi dapat meningkatkan pendapatan perusahaan sebesar 5% hingga 15% dan memperbaiki tingkat konversi penjualan hingga 10% hingga 15%. Selain itu, sistem ini juga memungkinkan perusahaan untuk memanfaatkan data besar dan teknik machine learning untuk memahami pola perilaku pengguna, sehingga dapat memberikan rekomendasi yang lebih akurat dan relevan. Dalam konteks e-commerce, sistem rekomendasi telah terbukti efektif dalam meningkatkan penjualan; misalnya, sekitar 35% dari pembelian di Amazon berasal dari rekomendasi produk. Dengan demikian, sistem rekomendasi tidak hanya berfungsi sebagai alat untuk menemukan konten yang diinginkan tetapi juga sebagai pendorong utama dalam strategi pemasaran modern.

Sistem rekomendasi anime telah muncul sebagai solusi penting di tengah meningkatnya popularitas anime di seluruh dunia. Dengan ribuan judul yang tersedia, pengguna sering kali merasa kewalahan dalam memilih anime yang sesuai dengan selera mereka. Oleh karena itu, sistem ini dirancang untuk memberikan rekomendasi yang lebih personal berdasarkan preferensi individu, seperti genre, tema, dan rating. Metode yang digunakan dalam sistem rekomendasi bervariasi, termasuk content-based filtering dan collaborative filtering, yang memungkinkan analisis mendalam terhadap data pengguna dan konten anime itu sendiri. Dengan memanfaatkan data besar dari platform seperti MyAnimeList, sistem ini tidak hanya meningkatkan pengalaman menonton tetapi juga membantu pengguna menemukan anime baru yang mungkin mereka nikmati. Selain itu, sistem rekomendasi juga memberikan manfaat bagi penyedia layanan streaming dengan meningkatkan keterlibatan pengguna dan kepuasan secara keseluruhan.

Referensi:

[1] [Sistem Rekomendasi: Tingkatkan pengalaman pengguna dengan saran yang relevan dan dipersonalisasi](https://radyadigital.com/id/blog/sistem-rekomendasi-tingkatkan-pengalaman-pengguna-dengan-saran-yang-relevan-dan-dipersonalisasi) 

[2] [Apa itu mesin rekomendasi?](https://www.ibm.com/id-id/think/topics/recommendation-engine)

[3] [Perbandingan Cosine Similarity Dan Euclidean Distance Pada Model Rekomendasi Buku Dengan Metode ItemBased Collaborative Filtering](https://ejournal.unesa.ac.id/index.php/jinacs/article/download/50375/41575)

## 2.Business Understanding
### 2,1 Problem Statements

Berikut rumusan masalah yang akan diselesaikan dalam proyek ini:
- Metode Pengukuran kesamaan mana yang paling efektif dalam proyek ini?
- Langkah-langkah apa yang paling akurat dalam melakukan data preparation?
- Apakah sistem rekomendasi akurat dalam memberikan rekomendasi?

Dari rumusan masalah diatas, berikut goals yang ingin dicapai dalam proyek ini:
- Metode pengukuran kesamaan memiliki keakuratan yang tinggi.
- Data preparation yang dilakukan menghasilkan sistem rekomendasi yang membrikan akurasi yang tinggi.
- Sistem Rekomendasi dengan akurat memberikan rekomendasi.

Langkah-langkah berikut adalah pendekatan yang digunakan untuk mencapai goals dan menjawab pertanyaan permasalahan sebelumya:
- Melakukan Data preparation seperti one-hot encoding pada fitur kategorial agar dalam pengembangan model mencapai akurasi diatas rata rata.
- Melakukan eksperimen dengan berbagai metode pengukuran kesamaan, seperti Cosine Similarity, Pearson Correlation, dan Euclidean distance.
- Melakukan analisis korelasi untuk memahami hubungan antara fitur dan preferensi pengguna.
- Melakukan evaluasi untuk mengukur keakuratan sistem rekomendasi.

## 3. Data Understanding

Sumber dataset: [Anime Recommendations Database](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)

Sumber dataset yang digunakan memiliki 2 file dengan jenis file `.csv`, yaitu:
- anime.csv
- rating.csv

Kita hanya menggunakan dataset anime.csv untuk membuat sistem rekomendasi Content-Based Filtering

### 3.1 Exploratory Analysis Data Anime
| anime_id | name                              | genre                                                                 | type  | episodes | rating | members |
|----------|-----------------------------------|----------------------------------------------------------------------|-------|----------|--------|---------|
| 32281    | Kimi no Na wa.                   | Drama, Romance, School, Supernatural                                | Movie | 1        | 9.37   | 200630  |
| 5114     | Fullmetal Alchemist: Brotherhood | Action, Adventure, Drama, Fantasy, Magic, Military                  | TV    | 64       | 9.26   | 793665  |
| 28977    | Gintama°                         | Action, Comedy, Historical, Parody, Samurai, Sci-Fi                 | TV    | 51       | 9.25   | 114262  |
| 9253     | Steins;Gate                      | Sci-Fi, Thriller                                                    | TV    | 24       | 9.17   | 673572  |
| 9969     | Gintama&#039;                    | Action, Comedy, Historical, Parody, Samurai, Sci-Fi                 | TV    | 51       | 9.16   | 151266  |
...
###### Tabel 3.1 Tabel data anime
#### 3.1.1 Deskripsi Variabel
Berikut variabel yang terdapat dalam dataset anime.csv:
- anime_id : Index setiap anime
- name : Judul anime, judul masih dalam bahasa jepang.
- genre : Genre anime, hasil dari kategorisasi pengelompokan.
- type : Jenis penyiaran, media penyiaran yang digunakan.
- episodes : Jumlah episode dalam satu anime.
- rating : Rating anime dengan nilai rata-rata seluruh rating yang diberikan pengguna
- members : Jumlah member yang bergabung dalam komunitas anime.

Diketahui jumlah baris dari data anime sebanyak 12294 entri. Namun terdapat beberapa baris data memilki nilai kosong atau null.

#### 3.1.2 Univariate Analysis
##### 3.1.2.1 Categorial Feature
Varibel yang tergolong dalam fitur kategori atau diskrit adalah name, genre, dan type.

**name**: jumlah variabel name dalam data anime sebanding dengan jumlah data yaitu sebanyak 12294 entri. Judul anime atau variabel yang digunakan masih berbahasa jepang belum ada terjemahan ke inggris maupun ke indonesia.

**genre**: Genre anime yang diketahui dalam data anime memiliki jumlah sebanyak 48. Namun kebanyakan anime memiliki genre lebih dari satu. Jadi anime memiliki genre dari kombinasi genre-genre yang ada.

![Distribusi Variabel Genre](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission2_ML_Terapan/assets/distribusi_genre.png?raw=true)
###### Gambar 3.1 Distribusi Variabel Genre

Dari distribusi diatas dapat disimpulkan bahwa genre comedy menjadi genre paling terbanyak dalam anime. Karena genre anime memiliki jumlah yang banyak maka dalam merekomendasikan anime nantinya akan memberi banyak pilihan bagi pengguna sistem rekomendasi.

**type**: Jenis penyiaran anime dalam data ini memiliki jumlah sebanyak 6.

![Distribusi Variabel type](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission2_ML_Terapan/assets/distribusi_type.png?raw=true)
###### Gambar 3.2 Distribusi Variabel type

Berdasarkan distribusi variabel type memilki informasi bahwa anime dengan type TV merupakan jenis penyiaran yang paling banyak digunakan oleh anime. Berikut penjelasan tiap type anime:
- Movie (Film): Anime yang diproduksi sebagai film layar lebar dan biasanya ditayangkan di bioskop sebelum dirilis dalam format lain seperti DVD/Blu-ray atau streaming. Durasi movie umumnya lebih panjang dari episode TV biasa. Contoh: Your Name., Spirited Away, film-film Studio Ghibli.
- TV (Serial Televisi): Ini adalah format anime yang paling umum, disiarkan secara reguler di televisi dalam episode mingguan. Biasanya terdiri dari beberapa season (musim) dengan jumlah episode yang bervariasi. Contoh: Naruto, One Piece, Attack on Titan.
- OVA (Original Video Animation): Anime yang dirilis langsung dalam format video rumahan seperti VHS, LaserDisc, DVD, atau Blu-ray, tanpa penayangan di televisi atau bioskop sebelumnya. OVA sering kali berupa spin-off, side story, atau extra episode dari serial TV yang populer. Contoh: Hellsing Ultimate, beberapa episode bonus dari serial TV.
- Special (Spesial): Episode khusus yang biasanya lebih pendek dari episode TV biasa dan sering kali ditayangkan sebagai tambahan atau tie-in dengan serial TV yang sedang berjalan. Spesial bisa berupa rekap episode, episode omake (ekstra humor), atau cerita pendek yang tidak termasuk dalam alur utama.
- Music (Video Musik): Anime yang diproduksi sebagai video musik untuk lagu tertentu. Durasi biasanya pendek, sesuai dengan durasi lagu.
- ONA (Original Net Animation): Anime yang dirilis secara eksklusif di internet melalui platform streaming atau situs web. ONA sering kali memiliki durasi episode yang lebih pendek dari serial TV dan bisa berupa format eksperimental. Contoh: Hetalia, Ninja Slayer From Animation

##### 3.1.2.2 Numerical Feature
Dalam dataset anime, yang tergolong dalam fitur numerik adalah rating dan members

**rating**: Diketahui bahwa nilai minimun rating adalah -1, dari sumber dataset menyatakan bahwa -1 memiliki arti user tidak memberikan rating anime walaupun sudah menonton anime tersebut. Sedangkan untuk nilai maksimum rating adalah 10. Rata-rata dari penilaian yang diberikan ada di skor 6.

![Distribusi Variabel rating](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission2_ML_Terapan/assets/distribusi_rating.png?raw=true)
###### Gambar 3.3 Distribusi Variabel rating

**members**: Jumlah members paling terbanyak adalah Death Note sebanyak 1013917. Sedangkan Anime dengan members paling sedikit adalah Gou-chan. Moko to Chinjuu no Mori no Nakama-tachi	sebanyak 5 members. Tingkat kepopuleran anime bisa disimpulkan berdasarkan jumlah variabel members.

![Distribusi Variabel members](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission2_ML_Terapan/assets/distribusi_members.png?raw=true)
###### Gambar 3.4 Distribusi Variabel members

**episodes**: Jumlah episodes setiap anime memiliki variasi yang beragam. Namun untuk anime bertipe movie hanya memiliki 1 episode, dikarenakan anime yang ditayangkan di bioskop hanya dapat memutar 1 episode. 

![Distribusi Variabel episodes](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission2_ML_Terapan/assets/distribusi_episode.png?raw=true)
###### Gambar 3.5 Distribusi Variabel Episodes

#### 3.1.3 Multivariate Analysis 
Sebelumnya fitur numerik pada data anime adalah episodes, rating, dan members. Ketiga fitur numerik ini dapat dilihat skor korelasinya untuk melihat hubungan antar variabel, seberapa kuat dan lemahnya.

![Heatmap rating dengan members](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission2_ML_Terapan/assets/heatmap_rating_members.png?raw=true)
###### Gambar 3.6 Heatmap rating dengan members

Fitur rating dan members memiliki skor korelasi yang cukup tinggi yaitu diatas 50%. Hal ini masuk akal dikarenakan anime dengan rating yang tinggi kebanyakan memiliki jumlah members yang tinggi juga. Semakin tinggi rating maka akan semakin populer anime tersebut. Banyak dari platform situs streaming online anime, anime dengan rating paling tinggi selalu ditampilkan di halaman pertama yang menunjukan rating dijadikan sebagai variabel rekomendasi non-personalized kebanyakan platform streaming anime.

![Rating Distribution by Anime Type](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission2_ML_Terapan/assets/rating_type.png?raw=true)
###### Gambar 3.7 Rating Distribution by Anime Type

- Anime dengan tipe Movie dan TV cenderung mendapatkan rating yang lebih tinggi dan lebih konsisten dibandingkan tipe lainnya.
- Anime dengan tipe Music cenderung mendapatkan rating yang lebih rendah.
- Tipe OVA, Special, dan ONA memiliki variasi rating yang lebih besar dan cenderung memiliki beberapa anime dengan rating yang sangat rendah.
- Keberadaan outlier menunjukkan adanya beberapa anime dengan rating yang sangat tinggi atau sangat rendah di setiap tipe.


#### 3.1.4 Data Preparation
Data preparation adalah langkah krusial dalam pengembangan model analisis data. Proses ini melibatkan pembersihan, transformasi, dan pengorganisasian data mentah agar siap digunakan dalam analisis dan pemodelan. Tanpa data preparation yang tepat, kualitas data yang digunakan dapat terpengaruh, yang pada gilirannya akan memengaruhi hasil analisis dan keputusan yang diambil.

##### 3.1.4.1 Cleaning Data
Kolom data dengan value null akan dihapus untuk menghindari bias.

| Column       | Non-Null Count |
|--------------|----------------|
| anime_id     | 0              |
| name         | 0              |
| genre        | 62             |
| type         | 25             |
| episodes     | 0              |
| rating       | 230            |
| members      | 0              |
| first_genre  | 0              |
###### Tabel 3.1 Missing Value

Berdasarkan informasi diatas, genre, type, dan rating memiliki nilai null. Langkah yang paling tepat menanggani missing value dalam proyek ini adalah menghapusnya. Alasannya adalah untuk meminimalkan sistem rekomendasi bias pada ke variabel tertentu. Baris yang dihapus hanyalah baris yang memiliki value null di fitur genre. Karena genre akan digunakan sebagai item di sistem content based filtering

##### 3.1.4.2 Feature Engineering
Dikarenakan fitur yang diguankan pada sistem rekomendasi content based filtering (CBF) hanyalah anime_id, name, dan genre. Maka fitur selain fitur tersebut tidak akan digunakan pada dataframe yang mana akan dijadikan sebagai input sistem rekomendasi CBF.

| anime_id | name                              | genre                                                                 |
|----------|-----------------------------------|----------------------------------------------------------------------|
| 32281    | Kimi no Na wa.                   | Drama, Romance, School, Supernatural                                |
| 5114     | Fullmetal Alchemist: Brotherhood | Action, Adventure, Drama, Fantasy, Magic, Military                  |
| 28977    | Gintama°                         | Action, Comedy, Historical, Parody, Samurai, Sci-Fi                 |
| 9253     | Steins;Gate                      | Sci-Fi, Thriller                                                    |
| 9969     | Gintama&#039;                    | Action, Comedy, Historical, Parody, Samurai, Sci-Fi                 |
...
###### Tabel 3.2 Final CBF

Dalam proses TF-IDF Vectorization, tanda hubung dan spasi akan memisahkan kata. Oleh karena itu, untuk genre Sci-Fi dan Slice of Life, representasi akan diubah menjadi "scifi" dan "sliceoflife" untuk memastikan genre tersebut diperlakukan sebagai satu fitur.
```
cbf_anime.loc[cbf_anime['genre'].str.contains('Sci-Fi', na=False), 'genre'] = cbf_anime['genre'].str.replace('Sci-Fi', 'scifi')

cbf_anime.loc[cbf_anime['genre'].str.contains('Slice of Life', na=False), 'genre'] = cbf_anime['genre'].str.replace('Slice of Life', 'sliceoflife')
```

Penggunaan `TfidfVectorizer` dari scikit-learn untuk memproses genre anime, input yang paling umum dan efisien adalah list string (di mana setiap string mewakili genre anime). Maka perlu dilakukan pengoversian data ke bentuk list.

```
# Mengonversi data series ‘anime_id’ menjadi dalam bentuk list
anime_id = cbf_anime['anime_id'].tolist()

# Mengonversi data series 'name' menjadi dalam bentuk list
anime_name = cbf_anime['name'].tolist()

# Mengonversi data series 'genre' menjadi dalam bentuk list
anime_genre = cbf_anime['genre'].tolist()
```

Sebelum menggunakan `TfidfVectorizer` untuk processing fitur, perlu dilakukannya one-hot encoding atau mengubah fitur kategori ke fitur numerik. ne-hot encoding adalah teknik yang penting dalam pengolahan data kategori untuk machine learning, karena mengubah data kategori menjadi representasi numerik yang dapat diproses oleh algoritma. Banyak algoritma machine learning memerlukan input dalam bentuk numerik, dan one-hot encoding menyediakan solusi dengan mengonversi setiap kategori menjadi vektor biner (0 dan 1). 

![One-hot Encoding](https://github.com/akbariffianto/ml-terapan-submission/blob/main/Submission2_ML_Terapan/assets/one-hot.png?raw=true)
###### Gambar 3.8 One-hot Encoding

Hal ini membantu meminimalkan potensi bias dalam model, karena setiap kategori ditransformasikan secara independen tanpa hubungan ordinal yang mungkin ada di antara mereka. Selain itu, one-hot encoding meningkatkan interpretabilitas hasil, memungkinkan pengguna untuk lebih mudah memahami kontribusi setiap kategori terhadap prediksi. Dalam banyak kasus, teknik ini juga dapat meningkatkan performa model, terutama pada model linear regresi dan klasifikasi, dengan menjaga keragaman fitur yang ada. Oleh karena itu, one-hot encoding merupakan langkah fundamental dalam persiapan data sebelum aplikasi machine learning, memastikan bahwa data kategori dapat diproses secara efektif dan akurat.

```
genre_list = []

# Membuat daftar genre unik
for index in fix_anime.index:
    temp = fix_anime['genre'][index].split(',')
    for i in temp:
        if i not in genre_list:
            genre_list.append(i)

onehot_df = pd.DataFrame(0, index=fix_anime.index, columns=genre_list)

# Mengisi nilai 1 untuk genre yang sesuai
for index in fix_anime.index:
    temp = fix_anime['genre'][index].split(',')
    for i in temp:
        onehot_df.loc[index, i] = 1

fix_anime = pd.concat([fix_anime, onehot_df], axis=1).fillna(0)
print(fix_anime.head())
```
Setelah melakukan one-hot encoding, langkah selanjutnya adalah menggunakan TF-IDF Vectorization. Sebelumnya kenapa langkah ini penting dilakukan? TF-IDF merupakan teknik untuk memberikan bobot pada setiap kata dalam sebuah dokumen berdasarkan frekuensi kemunculannya dalam dokumen tersebut (TF) dan seberapa langka kata tersebut di seluruh koleksi dokumen (IDF).

- Term Frequency (TF): Mengukur seberapa sering sebuah kata muncul dalam sebuah dokumen. Semakin sering sebuah kata muncul dalam dokumen, semakin tinggi nilai TF-nya.
- Inverse Document Frequency (IDF): Mengukur seberapa langka sebuah kata di seluruh koleksi dokumen. Semakin langka sebuah kata, semakin tinggi nilai IDF-nya. Kata-kata yang sangat umum (seperti "dan," "atau," "yang") memiliki nilai IDF yang rendah karena muncul di hampir semua dokumen.

Dalam konteks rekomendasi anime berdasarkan genre, TF-IDF dapat membantu mengidentifikasi genre yang paling penting dan membedakan antara anime yang berbeda. Misalnya, jika kata "action" muncul berkali-kali dalam deskripsi genre suatu anime dan kata tersebut relatif jarang muncul di deskripsi genre anime lain, maka kata "aksi" akan memiliki bobot TF-IDF yang tinggi untuk anime tersebut, menandakan bahwa genre action sangat relevan dengan anime tersebut.

```
from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data genre
tf.fit(fix_anime['genre'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()
```

Dalam proyek ini menggunakan library sklearn untuk menggunakan  `TfidfVectorizer`

## 4. Modeling
Setelah menyiapkan data sebelum melakukan pengembangan model, selanjutnya adalah pembuatan model sistem rekomendasi dengan pengukuran kesamaan Cosine Similarity dan Euclidean Distance

### 4.1 Cosine Similarity
Cosine similarity adalah sebuah metode matematika yang digunakan dalam sistem rekomendasi untuk mengukur kemiripan antara dua entitas, seperti dokumen, profil pengguna, atau atribut produk. Metode ini berbasis pada prinsip kosinus antara dua vektor yang saling tegak lurus dalam ruang Euclid. 
Proses awal dalam menggunakan cosine similarity adalah mengkonversi dokumen atau atribut ke dalam wujud vektor. Misalnya, dalam sistem rekomendasi film, setiap film dapat direpresentasikan sebagai vektor yang terdiri dari bobot-bobot kata-kata yang muncul dalam sinopsis atau reviewnya
```
Sim(q, dj) = (∑ (qi * dij)) / (√(∑ (qi²)) * √(∑ (dij²)))
```
Keterangan:
- Sim(q, dj) adalah nilai kosinus similarity antara query (q) dan dokumen (dj).
- qi adalah bobot kata ke-i dalam query.
- di, j adalah bobot kata ke-i dalam dokumen.
- Panjang vektor query dan dokumen dikalikan untuk mengnormalisasi hasil.

Nilai kosinus similarity berkisar antara -1 hingga +1. Semakin dekat nilai ke 1, semakin mirip dua entitas tersebut. Sebaliknya, semakin dekat nilai ke -1, semakin tidak mirip mereka. Angka 0 menunjukkan bahwa dua entitas sama sekali tidak mirip

Kelebihan Cosine Similarity
- Tidak terpengaruh panjang dokumen: Mampu membandingkan dokumen dengan panjang berbeda secara efektif karena fokus pada sudut antar vektor, bukan panjangnya.
- Mudah dipahami dan diinterpretasi: Hasilnya berkisar antara -1 (tidak mirip) hingga 1 (sangat mirip), dengan 0 berarti tidak ada kemiripan.
- Efektif dalam berbagai aplikasi: Berguna dalam deteksi plagiarisme, sistem rekomendasi, dan pencarian informasi, terutama untuk data berbasis teks.
- Sensitif terhadap proporsi kata: Memperhitungkan proporsi kata yang sama antar dokumen, memberikan pengukuran kemiripan teks yang akurat.


Kekurangan Cosine Similarity
- Tidak memperhitungkan urutan kata: Tidak mempertimbangkan konteks yang diberikan oleh urutan kata, sehingga informasi kontekstual penting bisa hilang.
- Rentan terhadap vektor sparsity: Representasi vektor bisa sangat jarang (sparse) pada data teks yang besar dan beragam, yang dapat memengaruhi akurasi pengukuran.
- Dipengaruhi stop words: Jika stop words (kata umum yang kurang bermakna) tidak dihapus, pengukuran kemiripan bisa kurang akurat karena stop words mendominasi vektor.
- Terbatas dalam menangkap nuansa semantik: Tidak memahami makna atau hubungan semantik antar kata, seperti sinonim atau frasa serupa.

#### 4.1.1 Pembuatan Model Cosine Similarity
```
from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim
```
Proyek ini menggunakan library sklearn untuk menghitung kesamaan cosine similarity. Kode ini mengambil representasi numerik anime (dalam bentuk matriks TF-IDF) dan menghitung seberapa mirip setiap anime dengan anime lainnya berdasarkan representasi tersebut. Hasilnya berupa matriks yang menunjukkan tingkat kesamaan antar setiap pasangan anime. Matriks ini kemudian dapat digunakan untuk membuat rekomendasi: jika sebuah anime mirip dengan anime yang disukai pengguna, maka anime tersebut direkomendasikan.

### 4.2 Euclidean Distance
Euclidean distance adalah metode yang digunakan dalam sistem rekomendasi untuk mengukur jarak antara dua titik dalam ruang multidimensi, yang sering kali mewakili fitur atau atribut dari item atau pengguna. Dalam konteks sistem rekomendasi, Euclidean distance menghitung seberapa mirip dua item atau pengguna berdasarkan nilai-nilai numerik mereka.

Euclidean distance dihitung menggunakan rumus:
```
D = √(∑ᵢ₌₁ⁿ(xᵢ - yᵢ)²)
```
di mana D adalah jarak Euclidean antara dua titik x dan y, dan n adalah jumlah dimensi (fitur) yang dibandingkan. Semakin kecil nilai jarak ini, semakin mirip kedua item atau pengguna tersebut.

Kelebihan dari Euclidean distance adalah kemudahan dalam interpretasi dan penerapannya dalam berbagai konteks. Namun, kekurangan utamanya adalah sensitivitas terhadap skala data; fitur dengan rentang nilai yang lebih besar dapat mendominasi perhitungan jarak, sehingga penting untuk melakukan normalisasi data sebelum menghitung jarak.

#### 4.1.1 Pembuatan Model Euclidean Distance
```
from sklearn.metrics.pairwise import euclidean_distances

euclidean_sim = euclidean_distances(tfidf_matrix)
euclidean_sim

euclidean_sim_df = pd.DataFrame(euclidean_sim, index=fix_anime['name'], columns=fix_anime['name'])
print('Shape:', euclidean_sim_df.shape)

euclidean_sim_df.sample(5, axis=1).sample(10, axis=0)
```

Kode ini menghitung jarak Euclidean antar anime berdasarkan representasi TF-IDF mereka, menyimpan hasilnya dalam DataFrame dengan nama anime sebagai indeks dan kolom, dan kemudian menampilkan sampel acak dari DataFrame tersebut. Ini memberikan cara yang mudah dibaca dan diakses untuk melihat seberapa "berbeda" setiap anime satu sama lain berdasarkan genre mereka. Semakin kecil jarak Euclidean, semakin mirip kedua anime tersebut.

## 5. Evaluation
Metrik Evaluasi yang digunakan untuk mengukur model mana yang paling akurat dalam merekomendasikan anime berdasarkan genre. Apabila sistem rekomendasi menggunakan metode Content-Based Filtering maka metrik evaluasi yang paling tepat adalah seperti berikut:

```
P = (Jumlah rekomendasi yang relevan) / (Jumlah total item yang direkomendasikan)
```
Precision adalah metrik evaluasi yang penting dalam content-based filtering karena mengukur seberapa tepat rekomendasi yang diberikan sistem. Presisi yang tinggi menunjukkan bahwa sistem efektif dalam merekomendasikan item yang relevan dengan preferensi pengguna berdasarkan konten item tersebut.

Berikut tiap topN Recommendations yang diberikan tiap model
### 5.1 Perbandingan Precision antar model
Setiap model akan memberikan rekomendasi anime apabila pengguna menyukai anime **Naruto** yang memiliki genre Action, Comedy, Martial Arts, Shounen, Super Power.

#### 5.1.1 Cosine Similarity
Berikut adalah output topN Recommendations model Cosine Similarity:
| No | Name                                        | Genre                                              |
|----|---------------------------------------------|---------------------------------------------------|
| 0  | Naruto: Shippuuden Movie 4 - The Lost Tower | Action, Comedy, Martial Arts, Shounen, Super Power |
| 1  | Boruto: Naruto the Movie - Naruto ga Hokage ni... | Action, Comedy, Martial Arts, Shounen, Super Power |
| 2  | Naruto Shippuuden: Sunny Side Battle        | Action, Comedy, Martial Arts, Shounen, Super Power |
| 3  | Naruto Soyokazeden Movie: Naruto to Mashin to... | Action, Comedy, Martial Arts, Shounen, Super Power |
| 4  | Boruto: Naruto the Movie                    | Action, Comedy, Martial Arts, Shounen, Super Power |
| 5  | Naruto x UT                                 | Action, Comedy, Martial Arts, Shounen, Super Power |
| 6  | Naruto: Shippuuden                          | Action, Comedy, Martial Arts, Shounen, Super Power |
| 7  | Naruto: Shippuuden Movie 3 - Hi no Ishi wo Tsu... | Action, Comedy, Martial Arts, Shounen, Super Power |
| 8  | Kyutai Panic Adventure!                    | Action, Martial Arts, Shounen, Super Power         |
| 9  | Naruto: Shippuuden Movie 6 - Road to Ninja | Action, Adventure, Martial Arts, Shounen, Super Power |
###### Tabel 5.1.1.1 TopN Recommendations Cosine Similarity
Dari kesepuluh anime yang direkomendasikan, semuanya relevan dan memiliki genre yang mirip, bisa disimpulkan nilai precisionnya seperti berikut:
```
P = 10 / 10
p = 1
```
Model memiliki keakuratan yang sangat akurat dalam merekomendasikan anime berdasarkan genre.

#### 5.1.2 Euclidean Distance
Berikut adalah output topN Recommendations model Euclidean Distance:

| No | Name                                        | Genre                                              |
|----|---------------------------------------------|---------------------------------------------------|
| 0  | Boruto: Naruto the Movie                   | Action, Comedy, Martial Arts, Shounen, Super Power |
| 1  | Naruto: Shippuuden                         | Action, Comedy, Martial Arts, Shounen, Super Power |
| 2  | Boruto: Naruto the Movie - Naruto ga Hokage ni... | Action, Comedy, Martial Arts, Shounen, Super Power |
| 3  | Naruto x UT                                 | Action, Comedy, Martial Arts, Shounen, Super Power |
| 4  | Naruto: Shippuuden Movie 4 - The Lost Tower | Action, Comedy, Martial Arts, Shounen, Super Power |
| 5  | Naruto: Shippuuden Movie 3 - Hi no Ishi wo Tsu... | Action, Comedy, Martial Arts, Shounen, Super Power |
| 6  | Naruto Shippuuden: Sunny Side Battle        | Action, Comedy, Martial Arts, Shounen, Super Power |
| 7  | Naruto Soyokazeden Movie: Naruto to Mashin to... | Action, Comedy, Martial Arts, Shounen, Super Power |
| 8  | Kyutai Panic Adventure!                    | Action, Martial Arts, Shounen, Super Power         |

Dari kesepuluh anime yang direkomendasikan, semuanya relevan dan memiliki genre yang mirip, bisa disimpulkan nilai precisionnya seperti berikut:
```
P = 10 / 10
p = 1
```
Model memiliki keakuratan yang sangat akurat dalam merekomendasikan anime berdasarkan genre.

## 6. Kesimpulan
Proyek ini bertujuan untuk mengembangkan sistem rekomendasi anime berbasis content-based filtering guna memberikan pengalaman pengguna yang lebih personal dan relevan. Analisis data awal menunjukkan dominasi genre comedy dan jenis penyiaran TV, yang mengindikasikan pentingnya fitur-fitur ini dalam model rekomendasi. Melalui tahapan data preparation yang cermat, termasuk one-hot encoding pada fitur genre, dan eksperimen dengan metode cosine similarity dan Euclidean distance, ditemukan bahwa cosine similarity dan Euclidean distance sama-sama efektif dalam mengidentifikasi anime dengan genre serupa, dengan keduanya mencapai precision 100%. Hasil ini menunjukkan bahwa, dalam konteks dataset dan metode evaluasi yang digunakan, semua rekomendasi yang diberikan oleh kedua model relevan dengan preferensi genre target.

Meskipun precision 100% adalah hasil yang sangat baik, perlu dilakukan analisis lebih lanjut untuk memastikan validitas hasil ini. Beberapa kemungkinan penyebab precision 100% dan langkah yang perlu dipertimbangkan adalah:
- Kesamaan data yang tinggi: Jika data anime memiliki kesamaan genre yang sangat tinggi, model mungkin akan selalu merekomendasikan anime dengan genre yang sama, sehingga menghasilkan precision tinggi. Perlu dianalisis distribusi genre dalam dataset.
- Metode evaluasi yang terlalu sederhana: Hanya menggunakan precision mungkin tidak cukup untuk mengevaluasi semua aspek sistem rekomendasi. Disarankan untuk menggunakan metrik lain seperti recall, F1-score, MAP, atau NDCG untuk evaluasi yang lebih komprehensif.

Implementasi sistem rekomendasi ini diharapkan dapat membantu pengguna menemukan anime yang sesuai preferensi mereka, serta meningkatkan kepuasan dan keterlibatan pengguna pada platform streaming anime. Sebagai langkah selanjutnya, akan dilakukan evaluasi dengan metrik yang lebih komprehensif seperti recall, F1-score, MAP, dan NDCG pada dataset yang lebih besar dan dengan jumlah rekomendasi yang lebih representatif. Selanjutnya untuk menemukan fitur yang paling berhubungan akan dilakukan penganalisis distribusi genre dalam dataset dan mempertimbangkan penambahan fitur lain seperti synopsis, user ratings, dan demografi pengguna untuk meningkatkan akurasi dan personalisasi rekomendasi. Proyek ini berpotensi untuk meningkatkan pengalaman menonton anime bagi pengguna dan memberikan kontribusi positif bagi perkembangan platform streaming anime di Indonesia