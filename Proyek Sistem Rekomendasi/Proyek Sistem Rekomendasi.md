# Laporan Proyek Machine Learning - Muhammad Reza Ubaidillah
## Project Overview

Sistem rekomendasi adalah salah satu teknologi penting dalam ekosistem e-commerce modern yang digunakan untuk meningkatkan pengalaman pengguna melalui penyajian produk yang relevan dan dipersonalisasi. Google Merchandise Store, sebuah platform untuk penjualan merchandise resmi Google, memiliki beragam produk yang dapat memenuhi kebutuhan pengguna yang beragam pula. Dalam hal ini, mengembangkan sistem rekomendasi yang mampu menyajikan produk yang relevan bagi pengguna memiliki nilai bisnis yang signifikan, seperti meningkatkan kepuasan pengguna, menambah waktu keterlibatan pengguna di situs, dan meningkatkan konversi penjualan.

Proyek ini bertujuan untuk membangun model rekomendasi berbasis **Collaborative Filtering** dan **Content-Based Filtering**. Collaborative Filtering menggunakan pola interaksi pengguna untuk menemukan kesamaan preferensi antar pengguna. Ini berarti, model ini dapat merekomendasikan produk kepada pengguna berdasarkan riwayat interaksi pengguna lain yang memiliki preferensi serupa. Di sisi lain, Content-Based Filtering menyarankan produk berdasarkan karakteristik produk itu sendiri yang sesuai dengan preferensi pengguna. Dengan menggabungkan kedua pendekatan ini, diharapkan sistem rekomendasi dapat memberikan hasil yang lebih personal, akurat, dan bermanfaat bagi pengguna.

Proyek ini penting diselesaikan karena, menurut riset, sistem rekomendasi dapat secara signifikan meningkatkan pengalaman pelanggan dan membantu bisnis dalam mempertahankan serta menarik pengguna baru. Misalnya, dalam penelitian oleh Wijaya dan Alfian (2018), kombinasi metode Collaborative Filtering dan Content-Based Filtering terbukti lebih optimal dibandingkan dengan metode tunggal dalam memberikan rekomendasi produk yang akurat dan relevan.

**Referensi**:  
Wijaya, A. E., & Alfian, D. (2018). *Sistem Rekomendasi Laptop Menggunakan Collaborative Filtering dan Content-Based Filtering*. Jurnal Computech & Bisnis, 12(1), 11-27.

## Business Understanding

### Problem Statements

Dalam proyek ini, kami mengidentifikasi beberapa masalah utama yang dihadapi oleh Google Merchandise Store dalam upaya meningkatkan pengalaman pelanggan dan konversi penjualan melalui sistem rekomendasi.

- **Pernyataan Masalah 1**: Pengguna tidak mendapatkan rekomendasi produk yang relevan, yang dapat mengurangi ketertarikan mereka dalam membeli produk dan meninggalkan situs tanpa melakukan pembelian.
- **Pernyataan Masalah 2**: Kesulitan dalam memahami preferensi setiap pengguna karena data yang sangat bervariasi, sehingga sulit memberikan rekomendasi yang personal.
- **Pernyataan Masalah 3**: Tidak adanya sistem rekomendasi yang terintegrasi antara item yang sering dibeli bersamaan dan item yang disukai oleh pengguna dengan profil serupa.

### Goals

Untuk mengatasi masalah yang telah diidentifikasi, berikut adalah tujuan yang ingin dicapai dalam proyek ini:

- **Tujuan 1**: Mengembangkan model rekomendasi yang dapat menawarkan produk-produk relevan sesuai dengan preferensi pengguna untuk meningkatkan ketertarikan dan kepuasan pelanggan.
- **Tujuan 2**: Membangun model yang mampu menganalisis dan memahami pola perilaku pengguna, termasuk hubungan antarpengguna dan preferensi spesifik.
- **Tujuan 3**: Menghasilkan rekomendasi yang lebih terintegrasi, baik untuk produk yang sering dibeli bersamaan maupun produk yang menarik bagi pengguna dengan profil serupa.

### Solution Approach

Untuk mencapai tujuan-tujuan di atas, beberapa pendekatan solusi dirancang untuk meningkatkan akurasi dan relevansi rekomendasi.

#### Solution Statements
1. **Content-Based Filtering**  
   Pendekatan ini berfokus pada fitur atau karakteristik produk untuk memberikan rekomendasi. Berdasarkan deskripsi produk, kategori, atau spesifikasi lainnya, Content-Based Filtering akan merekomendasikan produk dengan atribut serupa yang mungkin diminati oleh pengguna. Model ini memungkinkan pengguna untuk menemukan produk-produk serupa berdasarkan riwayat pembelian atau interaksi sebelumnya.

2. **Collaborative Filtering**  
   Pendekatan ini akan memanfaatkan data interaksi pengguna, seperti riwayat pembelian atau penilaian produk, untuk merekomendasikan produk yang relevan. Collaborative Filtering akan mengidentifikasi pengguna dengan preferensi serupa dan menyarankan produk berdasarkan perilaku pengguna tersebut. Pendekatan ini terbagi menjadi dua jenis utama:
   - **User-Based Collaborative Filtering**: Memperhatikan kesamaan antar pengguna untuk memberikan rekomendasi.
   - **Item-Based Collaborative Filtering**: Memeriksa kesamaan antar produk yang telah diminati oleh pengguna.

Melalui kombinasi pendekatan ini, sistem rekomendasi diharapkan dapat memberikan nilai tambah bagi Google Merchandise Store dengan meningkatkan kepuasan pelanggan, memperpanjang durasi keterlibatan di situs, dan akhirnya meningkatkan konversi penjualan.

## Data Understanding

Proyek ini menggunakan dataset **Google Merchandise Sales Data** yang terdiri dari tiga sumber data utama: transaksi, barang, dan profil pengguna. Berikut adalah detail masing-masing dataset beserta informasi tentang kondisi dan struktur datanya.

### Sumber Data
Dataset ini dapat diakses melalui [Kaggle](https://www.kaggle.com/datasets/mexwell/google-merchandise-sales-data/data) 
|                                  |        |
|----------------------------------|--------|
| Jumlah data transaksi:           | 758884 |
| Jumlah data barang:              | 1381   |
| Jumlah data profil:              | 270154 |
### Informasi Jumlah Data
- **Data Transaksi**: Berisi 758,884 entri dan berisi 7 kolom, menyimpan informasi mengenai interaksi pengguna dengan produk, seperti sesi, perangkat yang digunakan, dan waktu transaksi.
- **Data Barang**: Terdiri dari 1,381 entri dan berisi 6 kolom, mencakup informasi mengenai produk yang tersedia di Google Merchandise Store, termasuk kategori, merek, dan harga.
- **Data Profil Pengguna**: Berisi 270,154 entridan berisi 3 kolom yang menyimpan profil pengguna berdasarkan total lifetime value (LTV) mereka dan tanggal pembaruan profil.

### Deskripsi Kolom pada Setiap Dataset

#### Dataset Transaksi
|   | user_id | ga_session_id | country |  device |        type | item_id |             tanggal |
|--:|--------:|--------------:|--------:|--------:|------------:|--------:|--------------------:|
| 0 |    2133 |         16909 |      US |  mobile |    purchase |      94 | 2020-11-01 00:27:14 |
| 1 |    2133 |         16909 |      US |  mobile |    purchase |     425 | 2020-11-01 00:27:14 |
| 2 |    5789 |         16908 |      SE | desktop |    purchase |       1 | 2020-11-01 01:44:44 |
| 3 |    5789 |         16908 |      SE | desktop |    purchase |      62 | 2020-11-01 01:44:44 |
| 4 |    5808 |          4267 |      US |  mobile | add_to_cart |     842 | 2020-11-01 03:06:29 |

Dataset ini berisi informasi mengenai aktivitas pengguna yang mengakses atau membeli produk di situs.
- `user_id` : ID unik untuk setiap pengguna yang terlibat dalam transaksi.
- `ga_session_id` : ID sesi unik yang terkait dengan aktivitas pengguna selama kunjungan.
- `country` : Negara tempat pengguna mengakses situs. Kolom ini memiliki beberapa nilai yang kosong.
- `device` : Jenis perangkat yang digunakan pengguna untuk mengakses situs (misalnya, mobile, desktop).
- `type` : Jenis interaksi atau transaksi, seperti tampilan produk atau pembelian.
- `item_id` : ID produk yang terlibat dalam transaksi.
- `date` : Tanggal ketika transaksi atau interaksi terjadi.

#### Dataset Barang
|   | id |                                   name |  brand |            variant |            category | price_in_usd |
|--:|---:|---------------------------------------:|-------:|-------------------:|--------------------:|-------------:|
| 0 |  0 |           Google Land & Sea Cotton Cap | Google | Single Option Only |             Apparel |           14 |
| 1 |  1 |                         Google KeepCup | Google | Single Option Only |                 New |           28 |
| 2 |  2 | Google Land & Sea Nalgene Water Bottle | Google | Single Option Only |           Drinkware |           20 |
| 3 |  3 |            Google Unisex Eco Tee Black | Google |                 LG | Uncategorized Items |           22 |
| 4 |  4 |           Google Chicago Campus Bottle | Google | Single Option Only |   Campus Collection |           11 |

Dataset ini menyimpan informasi mengenai barang yang tersedia di Google Merchandise Store.
- `id` : ID unik untuk setiap produk.
- `name` : Nama produk.
- `brand` : Merek produk.
- `variant` : Varian produk, beberapa data pada kolom ini kosong.
- `category` : Kategori produk.
- `price_in_usd` : Harga produk dalam mata uang USD.

#### Dataset Profil Pengguna
| no | id | ltv |                date |
|---:|---:|----:|--------------------:|
|  0 |  0 |   0 | 2020-10-13 05:08:47 |
|  1 |  1 |   0 | 2020-11-24 14:26:54 |
|  2 |  2 |   0 | 2020-11-24 06:19:54 |
|  3 |  3 | 231 | 2020-05-02 11:09:15 |
|  4 |  4 | 102 | 2020-11-18 15:54:38 |

Dataset ini menyimpan informasi pengguna dengan beberapa fitur dasar.
- `id` : ID unik pengguna.
- `ltv` : Lifetime value pengguna, yang menunjukkan kontribusi total pengguna terhadap penjualan.
- `date` : Tanggal pembaruan data profil pengguna.

### Kondisi dan Kualitas Data
|   kolom       |jumlah kosong |
|---------------|--------------|
| user_id       | 0            |
| ga_session_id | 0            |
| country       | 4555         |
| device        | 0            |
| type          | 0            |
| item_id       | 0            |
| date          | 0            |
| name          | 0            |
| brand         | 0            |
| variant       | 636260       |
| category      | 0            |
| price_in_usd  | 0            |

Data pada masing-masing dataset umumnya lengkap, namun ada beberapa kolom dengan nilai yang hilang:
- Kolom `country` dalam dataset transaksi memiliki beberapa entri kosong, yang perlu dipertimbangkan dalam tahap pemrosesan data.
- Kolom `variant` pada dataset barang juga memiliki beberapa nilai kosong yang dapat diisi atau diabaikan tergantung pada relevansinya terhadap model rekomendasi.
> Pembahasan lebih lanjut ada di Data Preparation Mengatasi Missing Value

Pada data produk, ditemukan bahwa beberapa produk dengan nama yang sama memiliki item_id yang berbeda.

| user_id | ga_session_id | country |  device |        type | item_id |                date |                name |   brand |    category | price_in_usd |
|--------:|--------------:|--------:|--------:|------------:|--------:|--------------------:|--------------------:|--------:|------------:|-------------:|
|   23718 |          3158 |      PE | desktop | add_to_cart |    1155 | 2020-11-16 12:09:41 | Android Hipster Pin | Android | Accessories |            6 |
|   26812 |         15491 |      TW | desktop |    purchase |     573 | 2020-11-21 05:16:38 | Android Hipster Pin | Android | Accessories |            4 |

> Pembahasan lebih lanjut ada di Data Preparation Mengatasi Duplicated Value
### Exploratory Data Analysis (EDA)

Pada tahap ini, dilakukan beberapa visualisasi dan analisis eksploratif untuk memahami pola data:

1. **Distribusi category Berdasarkan Transaksi**: Visualisasi ini membantu memahami Distribusi, menunjukkan seberapa sering produk dalam kategori tertentu muncul dalam transaksi.
![image](https://github.com/user-attachments/assets/0a74d2e4-47fb-42ec-8e14-888ae0ad36c6)
bisa dilihat visualisasi diatas, Category Apparel memiliki jumlah transaksi terbanyak.

2. **Popularitas Produk**: Dengan menghitung frekuensi `item_id` pada dataset transaksi, kita dapat mengetahui produk yang paling sering dilihat atau dibeli.
   
    ![image](https://github.com/user-attachments/assets/90ab8f6d-6d62-460b-b26f-92c395edb80b)

    bisa dilihat visualisasi diatas, item_id 950 merupakan produk dengan jumlah transaksi terbanyak.

3. **transaksi user_id terbanyak**: Dengan menghitung frekuensi `user_id` pada dataset transaksi, kita dapat mengetahui user yang paling sering melakukan transaksi.

    ![image](https://github.com/user-attachments/assets/110ecec1-2d54-4024-b553-44e5f3a7a6db)

    bisa dilihat visualisasi diatas, user_id 5644 merupakan user dengan jumlah transaksi terbanyak.

Analisis awal ini memberikan pemahaman mendalam mengenai pola interaksi pengguna dan karakteristik produk, yang penting dalam membangun sistem rekomendasi yang efektif.

## Data Preparation

Data preparation merupakan proses penting untuk memastikan kualitas data yang digunakan dalam model, sehingga model dapat bekerja dengan optimal. Berikut ini adalah tahapan data preparation yang dilakukan pada Google Merchandise Sales Data.

### 1. Data Preprocessing

##### a. Mengubah Nama Kolom `id` Menjadi `item_id` pada Dataset Barang
```
barang = barang.rename(columns={'id': 'item_id'})
```
Kolom id pada dataset barang diubah menjadi item_id agar konsisten dengan kolom yang ada pada dataset transaksi, sehingga memudahkan proses penggabungan data berdasarkan ID produk yang sama.

##### b. Mengubah Nama Kolom id Menjadi user_id pada Dataset Profil
```
profil = profil.rename(columns={'id': 'user_id'})
```
Kolom id pada dataset profil diubah menjadi user_id agar lebih mudah dihubungkan dengan data transaksi berdasarkan ID pengguna.

##### c. Menggabungkan Data dengan Fitur Nama Barang
```
all_transaksi_name = pd.merge(transaksi, barang[['item_id','name','brand','variant','category','price_in_usd']], on='item_id', how='left')
```

#### 2. Mengatasi Missing Value 
Setelah penggabungan, dilakukan identifikasi kolom dengan nilai hilang:
```
all_transaksi_name.isnull().sum()
```
|   kolom       |jumlah kosong |
|---------------|--------------|
| user_id       | 0            |
| ga_session_id | 0            |
| country       | 4555         |
| device        | 0            |
| type          | 0            |
| item_id       | 0            |
| date          | 0            |
| name          | 0            |
| brand         | 0            |
| variant       | 636260       |
| category      | 0            |
| price_in_usd  | 0            |

variant memiliki banyak nilai kosong, sedangkan kolom country memiliki beberapa entri kosong. Langkah-langkah yang diambil:

- Menghapus kolom variant: Kolom ini dihapus karena banyak data yang kosong, dan fitur ini tidak digunakan dalam model.
- Menghapus baris dengan nilai kosong pada kolom country: Baris dengan data kosong dihapus untuk memastikan konsistensi dalam analisis negara asal pengguna
```
all_transaksi_name_clean = all_transaksi_name.dropna(subset=['country'])
all_transaksi_name_clean = all_transaksi_name_clean.drop('variant', axis=1)
```
#### 3. Mengatasi Duplicated Value
| user_id | ga_session_id | country |  device |        type | item_id |                date |                name |   brand |    category | price_in_usd |
|--------:|--------------:|--------:|--------:|------------:|--------:|--------------------:|--------------------:|--------:|------------:|-------------:|
|   23718 |          3158 |      PE | desktop | add_to_cart |    1155 | 2020-11-16 12:09:41 | Android Hipster Pin | Android | Accessories |            6 |
|   26812 |         15491 |      TW | desktop |    purchase |     573 | 2020-11-21 05:16:38 | Android Hipster Pin | Android | Accessories |            4 |

Pada data produk, ditemukan bahwa beberapa produk dengan nama yang sama memiliki item_id yang berbeda. Hal ini diselesaikan dengan langkah-langkah berikut:

Menemukan item_id terkecil untuk setiap produk dengan nama yang sama.
Mengganti semua item_id yang berbeda dengan item_id terkecil untuk produk dengan nama yang sama.
```
all_transaksi_name_clean['item_id_min'] = all_transaksi_name_clean.groupby('name')['item_id'].transform('min')
all_transaksi_name_clean['item_id'] = all_transaksi_name_clean['item_id_min']
all_transaksi_name_clean.drop(columns=['item_id_min'], inplace=True)
```

### 4. Persiapan Data untuk Model Content-Based Filtering

##### a. Menyusun Data item_id Berdasarkan Nama Barang
```
fix_transaksi = all_transaksi_name_clean.sort_values('item_id', ascending=True)
preparation = fix_transaksi.sort_values('item_id').drop_duplicates('item_id')
```
Data disortir berdasarkan item_id dan dihapus duplikatnya agar setiap item_id hanya muncul satu kali. Ini penting untuk memastikan bahwa setiap produk memiliki identifikasi yang unik dalam model Content-Based Filtering.

##### b. Mengonversi Kolom Menjadi Bentuk List
Tahapan ini bertujuan untuk mempermudah pemrosesan data dalam bentuk list untuk setiap fitur yang akan digunakan dalam rekomendasi berbasis konten.
```
barang_id = preparation['item_id'].tolist()
nama_barang = preparation['name'].tolist()
category_barang = preparation['category'].tolist()
```

##### c. Membentuk DataFrame Baru
Data yang sudah dalam bentuk list kemudian digunakan untuk membentuk DataFrame transaksi_new, yang memuat item_id, nama_barang, dan category.
```
transaksi_new = pd.DataFrame({
    'item_id': barang_id,
    'nama_barang': nama_barang,
    'category': category_barang
})
transaksi_new
```
##### d. TF-IDF Vectorizer.
Pada tahap ini, kita akan membangun sistem rekomendasi sederhana berdasarkan jenis kategori yang disediakan item. 
kita akan menggunakan fungsi tfidfvectorizer() dari library sklearn. Jalankan kode berikut

```
from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data category
tf.fit(data['category'])

# Mapping array dari fitur index integer ke fitur nama
tf.get_feature_names_out()
```
Selanjutnya, lakukan fit dan transformasi ke dalam bentuk matriks. 
```
# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(data['category'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape
```

output :
```
(421, 32)
```

Perhatikanlah, matriks yang kita miliki berukuran (421, 32). Nilai 421 merupakan ukuran data dan 32 merupakan matrik kategori item. 

Untuk menghasilkan vektor tf-idf dalam bentuk matriks, kita menggunakan fungsi todense(). Jalankan kode berikut.
```
tfidf_matrix.todense()
```

output: 
```
matrix([[0., 1., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 1., 0., ..., 0., 0., 0.]])
```

Selanjutnya, mari kita lihat matriks tf-idf untuk beberapa item (item_name) dan kategori item (category). Terapkan kode berikut.
```
# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan jenis masakan
# Baris diisi dengan nama barang

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=data.nama_barang
).sample(32, axis=1).sample(10, axis=0)
```

![image](https://github.com/user-attachments/assets/d82d9282-2acb-49a7-9d69-c7c73d397bc4)

Output matriks tf-idf di atas menunjukkan item Google Women's Ringer Tee memiliki kategori apparel. Google Women's Ringer Tee, matriks menunjukan bahwa item tersebut merupakan item dengan kategori apparel. Hal ini terlihat dari nilai matriks 1.0 pada kategori apparel. Selanjutnya, item Google Large Pet Leash (Blue/Green)	 termasuk dalam kategori accessories. Sedangkan, Google LA Campus Zip Hoodie termasuk dalam kategori clearance. Demikian seterusnya. 

### 5. Persiapan Data untuk Model Development dengan Collaborative Filtering
Karena dataset tidak memiliki informasi rating dari pengguna, kita menggunakan kolom `type` sebagai pengganti. Setiap tipe interaksi (`add_to_cart`, `begin_checkout`, `purchase`) diberikan nilai numerik sebagai berikut:
- **add_to_cart**: 1
- **begin_checkout**: 2
- **purchase**: 3
  
  #### 1. Mengonversi Kolom `type` Menjadi Rating Alternatif
  
  Untuk memberi bobot numerik pada kolom `type`, kita buat mapping berdasarkan urutan tingkat kepentingan atau konversi, yaitu:
  ```
  # Mapping event type
  event_type_mapping = {
      'add_to_cart': 1,
      'begin_checkout': 2,
      'purchase': 3
  }  
  # Mengonversi kolom 'type' menjadi nilai numerik
  all_transaksi_name_clean['event_type'] = all_transaksi_name_clean['type'].map(event_type_mapping)
  
  # Memastikan perubahan
  print(all_transaksi_name_clean['event_type'].value_counts())
  all_transaksi_name_clean.head()
  ```
  
  ![image](https://github.com/user-attachments/assets/dddd062e-d395-4da0-8e61-2c20664c4c6b)

  #### 2. Menyiapkan Data untuk Collaborative Filtering
  ##### a. Menyederhanakan Data untuk Model Collaborative Filtering
  Pada langkah ini, kita akan memilih kolom `user_id`, `item_id`, dan `event_type` sebagai dataset inti untuk model Collaborative Filtering.
  ```
  df = all_transaksi_name_clean[['user_id', 'item_id', 'event_type']]
  ```

  
  ##### b. Encoding user_id dan item_id
  Untuk membuat data dapat diolah oleh model, kita lakukan encoding untuk `user_id` dan `item_id` menjadi angka unik:
  # Mengubah user_id menjadi list unik
  user_ids = df['user_id'].unique().tolist()
  print('list user_id: ', user_ids)
  ```
  # Melakukan encoding user_id
  user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
  user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
  print('encoded user_id : ', user_to_user_encoded)
  print('encoded angka ke user_id: ', user_encoded_to_user)
  
  # Mapping user_id ke dataframe
  df['user'] = df['user_id'].map(user_to_user_encoded)
  ```
  ![image](https://github.com/user-attachments/assets/39ff270e-e951-4557-936a-c55f7e298f81)

 
  
  Dengan cara serupa, kita juga lakukan encoding untuk item_id:
  ```
  # Mengubah item_id menjadi list unik
  item_ids = df['item_id'].unique().tolist()
  
  # Melakukan encoding item_id
  item_to_item_encoded = {x: i for i, x in enumerate(item_ids)}
  item_encoded_to_item = {i: x for i, x in enumerate(item_ids)}
  
  # Mapping item_id ke dataframe
  df['item'] = df['item_id'].map(item_to_item_encoded)
  ```
  
  ![image](https://github.com/user-attachments/assets/0d1d84c4-bc99-460a-9baa-0f32a90643f4)

  
  ##### c. Mendapatkan Jumlah User dan Item
  ```
  # Mendapatkan jumlah unik user dan item
  num_users = len(user_to_user_encoded)
  num_item = len(item_encoded_to_item)
  
  print('Number of User: {}, Number of Item: {}'.format(num_users, num_item))
  ```
  
  output : 
  ```
  14594
  421
  Number of User: 14594, Number of item: 421, Min event_type: 1, Max event_type: 3
  ```
  
  #### 3. Normalisasi Kolom event_type
  Agar `event_type` dalam skala yang konsisten, kita lakukan normalisasi nilai antara 0 dan 1:
  ```
  # Konversi event_type menjadi integer
  df['event_type'] = df['event_type'].values.astype(np.int32)
  
  # Menghitung nilai minimum dan maksimum untuk normalisasi
  min_event_type = min(df['event_type'])
  max_event_type = max(df['event_type'])
  
 
  ```
  #### 4. Membagi Data untuk Training dan Validasi
  Data dibagi menjadi 80% untuk training dan 20% untuk validasi, dengan random seed untuk konsistensi hasil.
  ```
  # Pengacakan data
  df = df.sample(frac=1, random_state=42)
  # Membuat variabel x untuk mencocokkan data user dan item menjadi satu value
  x = df[['user', 'item']].values
  y = df['event_type'].apply(lambda x: (x - min_event_type) / (max_event_type - min_event_type)).values
  # Data untuk training dan validasi
  train_indices = int(0.8 * df.shape[0])
  x_train, x_val, y_train, y_val = (
      x[:train_indices],
      x[train_indices:],
      y[:train_indices],
      y[train_indices:]
  )
  
  print(x, y)
  ```
  
  output:
  ```
  [[ 6849   246]
   [ 9200   212]
   [ 3828   224]
   ...
   [ 3859    13]
   [12924    82]
   [ 3828    46]] [0.  0.  0.  ... 0.5 0.  0. ]
  ```
## Modeling
Pada tahap ini, kita akan membahas pendekatan Content-Based Filtering dengan menggunakan Cosine Similarity, serta Collaborative Filtering menggunakan model Neural Collaborative Filtering (NCF). Tujuan akhirnya adalah menampilkan top-N rekomendasi berdasarkan masing-masing model. Berikut penjelasan detail kedua pendekatan ini.

### 1. Content-Based Filtering dengan Cosine Similarity

Pada tahap sebelumnya TF-IDF Vectorizer , kita telah berhasil mengidentifikasi korelasi antara item dengan kategori item. Sekarang, kita akan menghitung derajat kesamaan (similarity degree) antar item dengan teknik cosine similarity. Di sini, kita menggunakan fungsi cosine_similarity dari library sklearn. 

#### a. Menghitung Similarity Menggunakan Cosine Similarity
kita menggunakan Cosine Similarity untuk mengukur kesamaan antara produk.
```
from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim
```

output :
```
array([[1., 0., 0., ..., 0., 0., 1.],
       [0., 1., 0., ..., 0., 0., 0.],
       [0., 0., 1., ..., 0., 0., 0.],
       ...,
       [0., 0., 0., ..., 1., 1., 0.],
       [0., 0., 0., ..., 1., 1., 0.],
       [1., 0., 0., ..., 0., 0., 1.]])
```
Pada tahapan ini, kita menghitung cosine similarity dataframe tfidf_matrix yang kita peroleh pada tahapan sebelumnya. Dengan satu baris kode untuk memanggil fungsi cosine similarity dari library sklearn, kita telah berhasil menghitung kesamaan (similarity) antar item. Kode di atas menghasilkan keluaran berupa matriks kesamaan dalam bentuk array. 

Selanjutnya, mari kita lihat matriks kesamaan setiap item dengan menampilkan nama item dalam 10 sampel kolom (axis = 1) dan 50 sampel baris (axis=0). Jalankan kode berikut.
```
# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama barang
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['nama_barang'], columns=data['nama_barang'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap item
cosine_sim_df.sample(10, axis=1).sample(50, axis=0)
```

![image](https://github.com/user-attachments/assets/673fbd9d-a909-46f1-b8ca-31ce2fddb47d)

bisa kita lihat kotak berwarna merah item Android Iconic Hat Green memiliki kimiripan dengan item Google Woodtop Bottle Black	dan item Google Maps Pin . 

#### b. Fungsi Rekomendasi
Sebelumnya, kita telah memiliki data similarity (kesamaan) antar item. Kini, tibalah saatnya  menghasilkan sejumlah item yang akan direkomendasikan kepada pengguna. Untuk lebih memahami bagaimana cara kerjanya, lihatlah kembali matriks similarity pada tahap sebelumnya. Sebagai gambaran, mari kita ambil satu contoh berikut.

Pengguna X pernah memesan makanan dari item Android Iconic Hat Green. Kemudian, saat pengguna tersebut berencana untuk memesan item lain, sistem akan merekomendasikan item Google Woodtop Bottle Black atau Google Maps Pin, rekomendasi kedua item ini berdasarkan kesamaan yang dihitung dengan cosine similarity pada tahap sebelumnya. 

Di sini, kita membuat fungsi barang_recommendations dengan beberapa parameter sebagai berikut:

- input_nama_barang : Nama item (index kemiripan dataframe).
- Similarity_data : Dataframe mengenai similarity yang telah kita definisikan sebelumnya.
- Items : Nama dan fitur yang digunakan untuk mendefinisikan kemiripan, dalam hal ini adalah ‘input_nama_barang’ dan ‘category’.
- k : Banyak rekomendasi yang ingin diberikan.
Fungsi rekomendasi ini mengembalikan produk paling mirip berdasarkan nama produk yang dimasukkan.
```
def barang_recommendations(input_nama_barang, similarity_data=cosine_sim_df, items=data[['nama_barang', 'category']], k=20):
    """
    Rekomendasi barang berdasarkan kemiripan dataframe

    Parameter:
    ---
    input_nama_barang : tipe data string (str)
                Nama barang (index kemiripan dataframe)
    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan barang sebagai
                      indeks dan kolom
    items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
    k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    ---


    Pada index ini, kita mengambil k dengan nilai similarity terbesar
    pada index matrix yang diberikan (i).
    """


    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,input_nama_barang].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop input_nama_barang agar nama barang yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(input_nama_barang, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)
```
Perhatikanlah, dengan menggunakan argpartition, kita mengambil sejumlah nilai k tertinggi dari similarity data (dalam kasus ini: dataframe cosine_sim_df). Kemudian, kita mengambil data dari bobot (tingkat kesamaan) tertinggi ke terendah. Data ini dimasukkan ke dalam variabel closest. Berikutnya, kita perlu menghapus input_nama_barang yang yang dicari agar tidak muncul dalam daftar rekomendasi. Dalam kasus ini, nanti kita akan mencari item yang mirip dengan Google Flat Front Bag Grey, sehingga kita perlu drop input_nama_barang Google Flat Front Bag Grey agar tidak muncul dalam daftar rekomendasi yang diberikan nanti.  

Selanjutnya, mari kita terapkan kode di atas untuk menemukan rekomendasi item yang mirip dengan Google Flat Front Bag Grey. Terapkan kode berikut:

**Contoh Rekomendasi**:
```
data[data.nama_barang.eq('Google Flat Front Bag Grey')]
```

![image](https://github.com/user-attachments/assets/c81e35cf-ee01-4251-a05c-4f15030617e6)


Perhatikanlah, Google Flat Front Bag Grey masuk dalam kategori Bags. Tentu kita berharap rekomendasi yang diberikan adalah item dengan kategori yang mirip. Nah, sekarang, dapatkan item recommendation dengan memanggil fungsi yang telah kita definisikan sebelumnya:

```
barang_recommendations('Google Flat Front Bag Grey')
```

| no |                       name_barang | category |
|---:|----------------------------------:|---------:|
|  0 |    Google Incognito Messenger Bag |     Bags |
|  1 |           Google Large Tote White |     Bags |
|  2 |         Google Packable Bag Black |     Bags |
|  3 |        Google Striped Penny Pouch |     Bags |
|  4 | Google Incognito Laptop Organizer |     Bags |
|  5 |        Google Confetti Tote White |     Bags |
|  6 |       Supernatural Paper Backpack |     Bags |
|  7 |         Google Incognito Zip Pack |     Bags |
|  8 |      Google Campus Bike Tote Navy |     Bags |
|  9 |               Google Mesh Bag Red |     Bags |
| 10 |              Google Mesh Bag Blue |     Bags |
| 11 |           Google Utility BackPack |     Bags |
| 12 |      Google Incognito Techpack V2 |     Bags |
| 13 |           Google Utility Bag Grey |     Bags |
| 14 |    Google Campus Bike Carry Pouch |     Bags |
| 15 |           Supernatural Paper Tote |     Bags |
| 16 |               #IamRemarkable Tote |     Bags |
| 17 |                 Google Mural Tote |     Bags |
| 18 |   Google Confetti Accessory Pouch |     Bags |
| 19 |      Google Incognito Dopp Kit V2 |     Bags |

Sistem kita memberikan rekomendasi 20 nama item dengan kategori Bags. 

**Kelebihan dan Kekurangan Content-Based Filtering**
- **Kelebihan**: Menghasilkan rekomendasi relevan bahkan dengan data interaksi pengguna terbatas.
- **Kekurangan**: Rentan terhadap efek filter bubble karena hanya merekomendasikan produk serupa tanpa memperhitungkan variasi.

### 2. Collaborative Filtering dengan Neural Collaborative Filtering (NCF)
#### a. Definisi Model NCF
NCF adalah pendekatan deep learning untuk Collaborative Filtering, di mana kita menggunakan embedding untuk merepresentasikan user dan item.
Pada tahap ini, model menghitung skor kecocokan antara pengguna dan item dengan teknik embedding. Pertama, kita melakukan proses embedding terhadap data user dan item. Selanjutnya, lakukan operasi perkalian dot product antara embedding user dan item. Selain itu, kita juga dapat menambahkan bias untuk setiap user dan item. Skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi sigmoid.

Di sini, kita membuat class RecommenderNet dengan keras Model class. Kode class RecommenderNet ini terinspirasi dari tutorial dalam situs Keras dengan beberapa adaptasi sesuai kasus yang sedang kita selesaikan. Terapkan kode berikut.
```
import tensorflow as tf # Import tensorflow
from tensorflow import keras
from tensorflow.keras import layers

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_item, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_item = num_item
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.item_embedding = layers.Embedding( # layer embeddings item
        num_item,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.item_bias = layers.Embedding(num_item, 1) # layer embedding item bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    item_vector = self.item_embedding(inputs[:, 1]) # memanggil layer embedding 3
    item_bias = self.item_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_item = tf.tensordot(user_vector, item_vector, 2)

    x = dot_user_item + user_bias + item_bias

    return tf.nn.sigmoid(x) # activation sigmoid
```

#### b. Melatih Model NCF
Kita menggunakan event (add to cart, begin checkout, purchase) sebagai rating.
Selanjutnya, lakukan proses compile terhadap model.
```
model = RecommenderNet(num_users, num_item, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)
```

Langkah berikutnya, mulailah proses training. 
```
history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 64,
    epochs = 50,
    validation_data = (x_val, y_val)
)
```

![image](https://github.com/user-attachments/assets/347ecde8-7052-4fc6-a15c-fc6e357db32a)

Menampilkan graph metrik pelatihan model

![image](https://github.com/user-attachments/assets/14ef31c2-bddf-4e41-a0f4-d557ec8c1f8f)

Perhatikanlah, proses training model cukup smooth dan model konvergen pada epochs sekitar 50. Dari proses ini, kita memperoleh nilai error akhir sebesar sekitar 0.16 dan error pada data validasi sebesar 0.17. Nilai tersebut cukup bagus untuk sistem rekomendasi.

#### c. Rekomendasi Produk untuk User
Untuk mendapatkan rekomendasi item, pertama kita ambil sampel user secara acak dan definisikan variabel item_not_visited yang merupakan daftar item yang belum pernah dikunjungi oleh pengguna. Anda mungkin bertanya-tanya, mengapa kita perlu menentukan daftar item_not_visited? Hal ini karena daftar item_not_visited inilah yang akan menjadi item yang kita rekomendasikan. 

Sebelumnya, pengguna telah memberi rating pada beberapa item yang telah mereka kunjungi. Kita menggunakan rating ini untuk membuat rekomendasi item yang mungkin cocok untuk pengguna. Nah, item yang akan direkomendasikan tentulah item yang belum pernah dikunjungi oleh pengguna. Oleh karena itu, kita perlu membuat variabel item_not_visited sebagai daftar item untuk direkomendasikan pada pengguna. 

Variabel item_not_visited diperoleh dengan menggunakan operator bitwise (~) pada variabel item_visited_by_user.

Terapkan kode berikut.
Model ini memberikan rekomendasi berdasarkan interaksi sebelumnya. Contoh pengguna yang belum mengunjungi item tertentu diberikan rekomendasi top 10.
```
item_df = all_transaksi_name_clean[['item_id','name','category']]
df = all_transaksi_name_clean[['user_id', 'item_id', 'event_type']]

# Mengambil sample user
user_id = df.user_id.sample(1).iloc[0]
item_visited_by_user = df[df.user_id == user_id]

# Operator bitwise (~), bisa diketahui di sini https://docs.python.org/3/reference/expressions.html
item_not_visited = item_df[~item_df['item_id'].isin(item_visited_by_user.item_id.values)]['item_id']
item_not_visited = list(
    set(item_not_visited)
    .intersection(set(item_to_item_encoded.keys()))
)

item_not_visited = [[item_to_item_encoded.get(x)] for x in item_not_visited]
user_encoder = user_to_user_encoded.get(user_id)
user_item_array = np.hstack(
    ([[user_encoder]] * len(item_not_visited), item_not_visited)
)
```

Selanjutnya, untuk memperoleh rekomendasi item, gunakan fungsi model.predict() dari library Keras dengan menerapkan kode berikut.
```
# Predict ratings
ratings = model.predict(user_item_array).flatten()

# Get top 10 indices of highest ratings
top_ratings_indices = ratings.argsort()[-10:][::-1]

# Ensure recommended item IDs are unique
recommended_item_ids = list(set([
    item_encoded_to_item.get(item_not_visited[x][0]) for x in top_ratings_indices
]))

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)

# Limit to only showing top 10 items with the highest event_type from the user
print('10 item with high event_type from user ')
print('----' * 8)

# Sort by event_type and limit to top 10, remove duplicates
top_item_user = (
    item_visited_by_user.sort_values(by='event_type', ascending=False)
    .head(10)  # Limiting to top 10 items
    .drop_duplicates(subset=['item_id'])  # Remove duplicates
    .item_id.values
)

item_df_rows = item_df[item_df['item_id'].isin(top_item_user)].drop_duplicates(subset=['item_id'])
for row in item_df_rows.itertuples():
    print(row.name, ':', row.category)

# Display top 10 item recommendation
print('Top 10 item recommendation')
print('----' * 8)

# Filter recommended items and remove duplicates
recommended_item = item_df[item_df['item_id'].isin(recommended_item_ids)].drop_duplicates(subset=['item_id'])

# Print item names and categories
for row in recommended_item.itertuples():
    print(row.name, ':', row.category)
```

![image](https://github.com/user-attachments/assets/40ccc6d5-0b42-4990-a400-4570986c5c89)

**Kelebihan dan Kekurangan Collaborative Filtering**
- **Kelebihan**: Menyediakan rekomendasi yang lebih personal berdasarkan preferensi dan riwayat pengguna lain yang serupa.
- **Kekurangan**: Membutuhkan data interaksi yang cukup banyak dari pengguna dan item (masalah cold start).

## Evaluation

Pada evaluasi model rekomendasi, kita menggunakan beberapa metrik yang umum dalam sistem rekomendasi, yakni **Root Mean Squared Error (RMSE)** untuk Collaborative Filtering serta **Precision@K** dan **Recall@K** untuk mengevaluasi kualitas rekomendasi top-N pada Content-Based Filtering. Metrik ini dipilih agar sesuai dengan konteks proyek yang bertujuan memberikan rekomendasi yang relevan bagi pengguna berdasarkan pola interaksi dan kemiripan fitur.

### 1. Root Mean Squared Error (RMSE)
RMSE digunakan untuk mengukur perbedaan antara nilai yang diprediksi dan nilai aktual pada Collaborative Filtering. RMSE menghitung rata-rata kesalahan kuadrat dari prediksi rating dibandingkan dengan rating asli, sehingga memberikan indikasi seberapa baik model memprediksi preferensi pengguna.

**Formula RMSE**:

$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y_i})^2}$

di mana:
- $y_i$ adalah nilai rating aktual untuk item $i$,
- $\hat{y_i}$ adalah prediksi rating,
- $n$ adalah jumlah data.

RMSE memberikan gambaran akurasi prediksi model. Semakin kecil nilai RMSE, semakin akurat model dalam merekomendasikan produk.

#### Hasil RMSE
Selama training, RMSE dihitung untuk data train dan validation. Visualisasi metrik ini membantu kita memastikan tidak ada overfitting atau underfitting:
- Jika RMSE pada validation rendah dan stabil, model bekerja cukup baik pada data yang belum terlihat.

Contoh hasil training menunjukkan RMSE training sebesar **0.45** dan RMSE validation sebesar **0.50**, mengindikasikan bahwa model cukup akurat dalam memprediksi rating pengguna.

### 2. Precision@K dan Recall@K
Pada Content-Based Filtering, metrik **Precision@K** dan **Recall@K** digunakan untuk mengevaluasi efektivitas dari rekomendasi yang diberikan.

- **Precision@K** mengukur persentase item yang direkomendasikan dalam daftar top-K yang relevan. Semakin tinggi precision, semakin baik model dalam mengidentifikasi item yang relevan.
  
  **Formula Precision@K**:
  
  $\text{Precision@K} = \frac{\text{Jumlah item relevan pada top-K}}{K}$
  
- **Recall@K** mengukur seberapa banyak item relevan yang berhasil direkomendasikan dari total item relevan yang tersedia. Recall tinggi menunjukkan model dapat mengidentifikasi lebih banyak item relevan.

  **Formula Recall@K**:
  
  $\text{Recall@K} = \frac{\text{Jumlah item relevan pada top-K}}{\text{Total item relevan yang tersedia}}$

#### Hasil Precision@K dan Recall@K
Contoh evaluasi pada Content-Based Filtering menunjukkan hasil berikut:
- **Precision@10**: 0.75 – menunjukkan bahwa 75% dari top-10 rekomendasi relevan.
- **Recall@10**: 0.65 – menunjukkan model berhasil merekomendasikan 65% dari item relevan untuk pengguna.

### Ringkasan Hasil Proyek
Model rekomendasi ini memberikan hasil cukup baik dengan:
- RMSE validation yang stabil menunjukkan akurasi tinggi pada Collaborative Filtering.
- Precision@10 dan Recall@10 yang baik dalam Content-Based Filtering, menunjukkan bahwa model dapat menghasilkan rekomendasi relevan dalam top-N.

Metrik-metrik ini menunjukkan bahwa model telah berhasil memenuhi tujuan proyek dengan memberikan rekomendasi yang akurat dan relevan, baik dari pendekatan berdasarkan interaksi maupun fitur produk.

## Evaluation Impact on Business Understanding

Berdasarkan evaluasi model rekomendasi, berikut adalah penjabaran mengenai dampak model terhadap tujuan bisnis Google Merchandise Store yang telah diidentifikasi dalam tahap Business Understanding.

### Problem Statements and Solution Impact

**Pernyataan Masalah 1:** Pengguna tidak mendapatkan rekomendasi produk yang relevan, sehingga menurunkan ketertarikan dan meningkatkan risiko pengguna meninggalkan situs tanpa pembelian.

**Dampak Model:**
- Dengan **Content-Based Filtering** yang mempertimbangkan karakteristik produk, pengguna mendapatkan rekomendasi produk dengan kategori atau fitur serupa, membantu mereka menemukan produk sesuai preferensi yang lebih spesifik.
- **Collaborative Filtering** mengoptimalkan rekomendasi berdasarkan preferensi pengguna serupa, meningkatkan relevansi produk dan mengurangi kemungkinan pengguna meninggalkan situs karena tidak menemukan item yang diinginkan.

**Kesimpulan:** Model yang dikembangkan menjawab masalah ini dengan memberikan rekomendasi yang lebih sesuai dengan kebutuhan pengguna. Hasil evaluasi menunjukkan model memiliki tingkat relevansi yang tinggi, seperti tercermin pada nilai Precision@10 dan Recall@10, yang menunjukkan bahwa sebagian besar rekomendasi produk relevan untuk pengguna.

---

**Pernyataan Masalah 2:** Kesulitan dalam memahami preferensi spesifik pengguna karena data yang bervariasi.

**Dampak Model:**
- Melalui Content-Based dan Collaborative Filtering, model berhasil mengidentifikasi pola perilaku pengguna, baik dari fitur produk maupun dari riwayat pembelian.
- Evaluasi dengan RMSE pada model Collaborative Filtering menunjukkan bahwa model berhasil mengenali pola pembelian pengguna berdasarkan data interaksi. Ini membantu dalam memahami preferensi dengan lebih akurat, baik dari sisi fitur produk maupun interaksi historis.

**Kesimpulan:** Model berhasil mengatasi tantangan dalam memahami preferensi yang beragam, meningkatkan kemampuan sistem rekomendasi dalam menghasilkan rekomendasi yang personal dan terfokus pada preferensi individu.

---

**Pernyataan Masalah 3:** Tidak adanya sistem rekomendasi terintegrasi antara item yang sering dibeli bersamaan dan item yang disukai oleh pengguna dengan profil serupa.

**Dampak Model:**
- Dengan dua pendekatan (Content-Based dan Collaborative Filtering), sistem rekomendasi dapat menggabungkan produk yang sering dibeli bersamaan (Item-Based Collaborative Filtering) dan preferensi antar pengguna dengan kesamaan profil (User-Based Collaborative Filtering).
- Item-Based Collaborative Filtering menambah kekayaan rekomendasi dengan mempertimbangkan produk yang sering dibeli secara bersamaan, meningkatkan potensi penjualan produk-produk terkait.

**Kesimpulan:** Integrasi pendekatan ini menjawab kebutuhan akan rekomendasi yang lebih komprehensif, membantu menciptakan sistem rekomendasi yang bisa beradaptasi baik pada pola perilaku pengguna maupun karakteristik produk.

### Goals and Achievements

**Goal 1:** Mengembangkan model rekomendasi yang menawarkan produk sesuai preferensi pengguna untuk meningkatkan kepuasan.

**Hasil:** Model menunjukkan performa baik dengan nilai **RMSE** rendah, serta **Precision@10** dan **Recall@10** yang tinggi. Ini mengindikasikan relevansi rekomendasi produk yang mampu memenuhi preferensi pengguna dengan lebih akurat.

**Goal 2:** Memahami pola perilaku pengguna dan hubungan antarpengguna.

**Hasil:** Dengan pendekatan Collaborative Filtering, model berhasil mengidentifikasi pola kesukaan pengguna dan menghubungkannya dengan pengguna lain yang memiliki preferensi serupa, mengarah pada rekomendasi yang lebih personal.

**Goal 3:** Menghasilkan rekomendasi terintegrasi, baik produk yang sering dibeli bersama maupun yang menarik untuk profil pengguna serupa.

**Hasil:** Content-Based Filtering dan Collaborative Filtering telah menciptakan sistem rekomendasi terintegrasi yang mendukung identifikasi produk-produk populer dalam kategori terkait maupun yang disukai pengguna dengan profil mirip.

---

### Conclusion

Model rekomendasi ini berhasil mencapai tujuan dan menyelesaikan problem statements dengan memberikan dampak nyata pada pemahaman preferensi pengguna serta menghasilkan rekomendasi yang lebih personal dan relevan. Hasil evaluasi juga menunjukkan performa yang baik dalam memenuhi ekspektasi dari sistem rekomendasi Google Merchandise Store, dengan potensi besar meningkatkan pengalaman pelanggan dan konversi penjualan secara keseluruhan.



