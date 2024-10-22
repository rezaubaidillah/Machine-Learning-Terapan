# Laporan Proyek Machine Learning - Muhammad Reza Ubaidillah
Di era digital ini, media sosial seperti Twitter memungkinkan individu untuk menyampaikan opini mereka secara terbuka terkait berbagai topik penting, seperti pemilihan umum, kebijakan pemerintah, atau produk komersial. Namun, dengan masifnya jumlah data, analisis manual menjadi tidak efektif dalam memahami persepsi publik. Oleh karena itu, model sentimen analisis menjadi solusi yang dapat membantu dalam mengidentifikasi sentimen masyarakat, apakah positif, negatif, atau netral, terhadap suatu topik.

Twitter sendiri telah mengambil beberapa langkah untuk menangani masalah ini, namun pendekatan manual dan otomatis yang ada belum sepenuhnya efektif. Salah satu cara untuk mengatasi tantangan ini adalah dengan memanfaatkan teknologi kecerdasan buatan, khususnya Natural Language Processing (NLP), untuk mengembangkan model klasifikasi sentimen yang dapat mengidentifikasi tweet negatif dan secara otomatis mengambil tindakan terhadap konten tersebut. Dengan menganalisis sentimen tweet, Twitter dapat secara proaktif meminimalkan konten yang merusak dan menciptakan lingkungan online yang lebih sehat.

- **Mengapa dan Bagaimana Masalah Ini Harus Diselesaikan**
Masalah konten negatif di media sosial, termasuk Twitter, memiliki dampak luas pada pengalaman pengguna. Ujaran kebencian dan konten ofensif dapat memicu konflik sosial, merusak reputasi platform, serta mengganggu kesehatan mental para pengguna. Meningkatnya jumlah pengguna media sosial setiap hari membuat pengawasan manual terhadap semua konten menjadi tidak mungkin dilakukan. Oleh karena itu, solusi berbasis machine learning, seperti analisis sentimen, menjadi penting dalam mengelola volume besar data yang dihasilkan oleh pengguna.
Model analisis sentimen berbasis NLP memungkinkan platform untuk mengenali emosi atau sentimen yang terkandung dalam teks, yang kemudian dikategorikan sebagai sentimen positif, netral, atau negatif. Melalui penerapan model ini, Twitter dapat lebih cepat mendeteksi dan memblokir konten berbahaya sebelum beredar luas. Implementasi solusi ini dapat meningkatkan pengalaman pengguna, menjaga komunitas tetap aman, serta memperkuat citra positif platform.

- Referensi: 
Fani, S. M., Santoso, R., & Suparti, S. (2021). Penerapan Text Mining Untuk Melakukan Clustering Data Tweet Akun Blibli Pada Media Sosial Twitter Menggunakan K-Means Clustering. Jurnal Gaussian, 10(4), 583-593.
  

## Business Understanding
### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Pernyataan Masalah 1: Penyebaran Konten Negatif di Twitter Twitter sering menjadi platform untuk menyebarkan ujaran kebencian, kekerasan verbal, dan konten negatif lainnya yang dapat membahayakan pengguna. Konten ini dapat menyebar dengan cepat dan berpotensi menyebabkan dampak negatif pada psikologis pengguna serta menimbulkan konflik sosial di dunia nyata.
- Pernyataan Masalah 2: Ketidakmampuan Pendekatan Manual dalam Memfilter Konten Dengan jumlah tweet yang sangat besar diposting setiap hari, pendekatan manual dalam memoderasi dan mengawasi konten negatif menjadi tidak mungkin dilakukan dengan efektif. Tanpa sistem otomatis yang kuat, konten berbahaya dapat lolos dari pengawasan.
- Pernyataan Masalah 3: Keterbatasan Algoritma dalam Mengenali Nuansa Bahasa Algoritma moderasi yang ada sering kali tidak mampu mengenali nuansa bahasa atau konteks dalam tweet, yang menyebabkan banyak tweet negatif tetap lolos karena tidak sesuai dengan pola kata-kata kasar yang sudah terdeteksi.

### Goals

- Jawaban Pernyataan Masalah 1: Mengurangi Penyebaran Konten Negatif di Twitter Tujuan utama adalah mengembangkan model klasifikasi sentimen yang dapat secara otomatis mendeteksi dan memblokir tweet negatif sebelum tersebar luas. Hal ini akan membantu mengurangi potensi konflik dan menciptakan lingkungan yang lebih aman bagi pengguna.
- Jawaban Pernyataan Masalah 2: Meningkatkan Efektivitas Moderasi Konten Sistem otomatis berbasis machine learning akan diimplementasikan untuk menggantikan metode manual, sehingga volume data besar yang dihasilkan dapat diawasi dan diproses secara real-time. Hal ini akan meningkatkan efisiensi moderasi konten.
- Jawaban Pernyataan Masalah 3: Meningkatkan Akurasi Pendeteksian Konten Negatif Menggunakan pendekatan NLP yang lebih canggih untuk menangani nuansa dan konteks bahasa yang kompleks, sehingga tweet negatif dapat dikenali dengan lebih baik bahkan ketika menggunakan bahasa yang halus atau tidak langsung.

### Solution statements
- **Linear Support Vector Classifier dengan Teknik Feature Engineering TF-IDF**
Untuk menyelesaikan permasalahan klasifikasi sentimen tweet, kami memutuskan untuk menggunakan LinearSVC sebagai algoritma utama. LinearSVC dipilih karena kemampuannya untuk menangani dataset teks besar dengan efisien, terutama saat menggunakan representasi fitur seperti TF-IDF. Algoritma ini secara khusus dioptimalkan untuk data yang dapat dipisahkan secara linier dan mampu menangani banyak fitur dengan waktu komputasi yang lebih cepat dibandingkan dengan SVM kernel non-linier.
- **Peningkatan Model dengan Hyperparameter Tuning**
Setelah membuat model baseline dengan LinearSVC, kami akan meningkatkan performa model melalui hyperparameter tuning. Beberapa parameter kunci yang akan disesuaikan termasuk:
    - C: Parameter regulasi yang mengontrol keseimbangan antara margin dan kesalahan klasifikasi.
    - penalty: Menentukan regulasi L2 yang menghindari overfitting.
    - loss: Memilih fungsi kerugian terbaik antara hinge atau squared_hinge.
    - max_iter: Mengatur jumlah iterasi maksimum untuk mencapai konvergensi optimal.
    
    Melalui proses GridSearchCV, model akan diuji dengan berbagai kombinasi parameter, dan model terbaik dipilih berdasarkan evaluasi metrik
- **Metrik Evaluasi**
Kinerja model akan dievaluasi menggunakan metrik berikut:
    - Precision: Mengukur persentase prediksi positif yang benar-benar positif.
    - Recall: Mengukur kemampuan model dalam mendeteksi seluruh tweet negatif.
    - F1-Score: Rata-rata harmonik antara precision dan recall, untuk memberikan gambaran seimbang tentang kinerja model.
    
    Dengan pendekatan ini, kita dapat memastikan bahwa model yang dibangun fokus pada akurasi dalam mendeteksi tweet negatif tanpa mengabaikan konteks penting yang relevan.
    > Penjelasan Metrik Evaluasi akan dibahas lebih lanjut pada bagian **Evaluation**.

## Data Understanding
Dalam proyek ini, data yang digunakan berasal dari dataset Twitter Sentiment Analysis yang tersedia di Kaggle. Dataset ini berisi tweet yang telah diberi label sentimen. Dataset dapat diakses melalui tautan berikut: [Twitter Sentiment Analysis Dataset.](https://www.kaggle.com/datasets/daniel09817/twitter-sentiment-analysis)

Dataset ini dirancang untuk tugas klasifikasi sentimen, di mana setiap tweet dikategorikan ke dalam tiga jenis sentimen: positif, negatif, atau other. Data ini akan digunakan untuk melatih model  Linear Support Vector Classifier (LinearSVC) dalam mendeteksi sentimen tweet secara otomatis.


### Informasi Data:
![image](https://github.com/user-attachments/assets/b57df407-5147-4af6-8c19-186a2b9b07c0)

- **Jumlah Data**: Dataset ini memiliki total **691248  baris** dan **2 kolom**.
- **Kondisi Data**: terdapat **4 missing value pada kolom text** dan terdapat **20825 duplicate value pada kolom text**, sehingga kita harus menghapus missing dan duplicate value lalu karena setiap tweet di dataset memiliki label sentimen dan teks tweet. Namun, data teks dapat mengandung simbol atau karakter khusus yang memerlukan pembersihan sebelum analisis.
- **Tautan Sumber Data**: [Twitter Sentiment Analysis Dataset](https://www.kaggle.com/datasets/daniel09817/twitter-sentiment-analysis).


### Variabel-variabel Twitter Sentiment Analysis Dataset adalah sebagai berikut:
- Text: Kolom ini berisi teks mentah dari tweet yang akan dianalisis. Ini adalah fitur utama yang akan diolah dengan teknik Natural Language Processing (NLP) dan feature engineering menggunakan TF-IDF untuk membangun representasi numerik dari setiap tweet.

- Label: Kolom ini mengindikasikan kategori sentimen dari tweet, dengan tiga label yang mungkin:
    - Positive: Tweet yang memiliki sentimen positif.
    - Negative: Tweet yang mengandung sentimen noegatif.
    - Neutral: Tweet yang tidak menunjukkan sentimen yang jelas atau netral.


**Exploratory Data Analysis (EDA)**:
1. Distribusi Label Sentimen:
   Menganalisis jumlah tweet untuk setiap label sentimen (positif, negatif, dan other) untuk memahami apakah data seimbang atau tidak.
   Untuk melihat sentimen pada data, kadang kita perlu melakukan visualisasi terhadap kata-kata dengan fungsi word cloud.
   
   ![image](https://github.com/user-attachments/assets/952333ab-5909-4e50-8124-f4acf79f8d14)

   Terlihat dari grafik kita memiliki dataset yang tidak seimbang pada dataset yang berlabel neutral . Meskipun demikian, ini tidak menjadi masalah yang signifikan karena kita melatih ulasan berlabel sentimen satu per satu, menggunakan label sentimen masing-masing ulasan.
3. Panjang Tweet:
   Menghitung rata-rata panjang tweet dalam karakter dan kata, serta visualisasi distribusi panjang tweet untuk melihat apakah ada pola tertentu yang relevan dengan klasifikasi sentimen.
   ![image](https://github.com/user-attachments/assets/ef753d5d-755a-403c-8e98-d217919424eb)
4. Frekuensi Kata-Kata Umum:
   Melakukan analisis frekuensi kata untuk tweet yang dikategorikan sebagai positif, negatif, atau other. Hal ini membantu mengidentifikasi kata-kata yang sering muncul dalam setiap kategori sentimen.
   ![image](https://github.com/user-attachments/assets/2dca8cca-11ed-44ac-888c-a833c6da2722)

   Ini adalah kata-kata yang paling sering muncul dalam dataset berlabel positif. Dari sana kita dapat mengenali beberapa kata kunci seperti good, easier, best dan perfect
   ![image](https://github.com/user-attachments/assets/d5eaea66-903c-4889-91b1-da67748324cd)

   Ini adalah kata-kata yang paling sering muncul dalam dataset berlabel negatif. Dari sana kita dapat mengenali beberapa kata kunci seperti problem, broken, poor dan wrong
   ![image](https://github.com/user-attachments/assets/9a6f56b7-6cdd-41c5-b164-d11a734ade0e)

   Ini adalah kata-kata yang paling sering muncul dalam dataset berlabel neutral. Dari sana kita dapat mengenali beberapa kata kunci seperti maybe, almost, might, dan possible
   
## Data Preparation
Pada tahap Data Preparation, dilakukan serangkaian langkah untuk mempersiapkan data agar siap digunakan dalam pemodelan machine learning. Setiap langkah diuraikan secara sistematis, beserta penjelasan mengapa tahapan tersebut diperlukan.

1. **Menghapus Nilai yang Hilang (Missing Values)**
Langkah pertama dalam persiapan data adalah memeriksa apakah terdapat nilai yang hilang (missing values) dalam dataset. Jika terdapat tweet atau label yang hilang, data tersebut akan dihapus.
    ```
    #Menghapus nilai yang hilang
    df.dropna(inplace=True)
    ```
    Tweet yang tidak memiliki teks atau label tidak akan memberikan kontribusi yang berarti bagi model dan dapat menurunkan performa model jika dibiarkan.
2. **Menghapus Duplikasi Data**
Data yang memiliki duplikasi, misalnya tweet yang sama diulang beberapa kali, akan dihapus untuk menghindari bias.
    ```
    # Menghapus tweet yang duplikat
    df.drop_duplicates(subset='Text', inplace=True)
    ```
    Menghilangkan duplikasi penting agar model tidak overfitting pada data tertentu. Tweet yang berulang dapat menyebabkan bias, di mana model mungkin terlalu fokus pada pola yang tidak mewakili keseluruhan data.
    
3. **Pembersihan Teks**
Tahap berikutnya adalah membersihkan teks dalam tweet. Langkah-langkah yang dilakukan termasuk:
    - Mengubah semua teks menjadi huruf kecil.
    - Menghapus tanda baca, angka, dan karakter khusus.
    - Menghapus URL dan mention (@username).
    - Menghapus stopwords (kata-kata umum yang tidak memiliki makna penting dalam analisis sentimen).
     ```
    import re
    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    
    # Daftar stopwords
    stop_words = set(stopwords.words('english'))
    
    # Fungsi untuk membersihkan teks
    def clean_text(text):
        text = text.lower()  # Mengubah teks menjadi huruf kecil
        text = re.sub(r'@\w+|http\S+', '', text)  # Menghapus mention dan URL
        text = re.sub(r'[^a-z\s]', '', text)  # Menghapus tanda baca dan angka
        text = ' '.join([word for word in text.split() if word not in stop_words])  # Menghapus stopwords
        return text
    
    df['clean_text'] = df['Text'].apply(clean_text)
    ```
    Pembersihan teks diperlukan untuk memastikan bahwa model tidak terganggu oleh karakter yang tidak relevan seperti tanda baca, URL, atau kata yang tidak berkontribusi dalam penentuan sentimen (misalnya stopwords). Langkah ini bertujuan agar model hanya mempelajari fitur penting yang merepresentasikan sentimen dalam teks.

4. **Tokenisasi dan Stemming/Lemmatization**
Tokenisasi adalah proses memecah teks menjadi kata-kata individu (tokens). Setelah itu, stemming atau lemmatization digunakan untuk mengubah kata menjadi bentuk dasar (misalnya, "running" menjadi "run").
    ```
    from nltk.stem import PorterStemmer

    ps = PorterStemmer()
    
    # Fungsi untuk tokenisasi dan stemming
    def stem_text(text):
        tokens = text.split()
        return ' '.join([ps.stem(word) for word in tokens])
    
    df['stemmed_text'] = df['clean_text'].apply(stem_text)

    ```
    Proses ini mengurangi kompleksitas bahasa dan memastikan bahwa kata-kata dengan makna yang sama dipertimbangkan sebagai satu entitas, misalnya "running" dan "run". Ini dapat membantu model fokus pada makna dasar dari kata, bukan variasi bentuk kata.
 5. **Transformasi Teks ke Dalam Bentuk TF-IDF**
Setelah teks dibersihkan dan diproses, langkah selanjutnya adalah mengubah teks menjadi representasi numerik menggunakan teknik Term Frequency-Inverse Document Frequency (TF-IDF). Teknik ini menghitung pentingnya suatu kata dalam dokumen dibandingkan dengan kata-kata lain di dalam seluruh kumpulan dokumen.   
    ```
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    tfidf = TfidfVectorizer(max_features=5000)  # Hanya menggunakan 5000 fitur teratas
    X = tfidf.fit_transform(df['stemmed_text'])
    y = df['Label']  # Label target
    ```
    TF-IDF membantu dalam memprioritaskan kata-kata yang lebih penting dalam konteks klasifikasi sentimen, sehingga kata-kata yang terlalu umum atau sering muncul tidak diberikan bobot yang berlebihan.
6. **Pembagian Data untuk Training dan Testing**
Langkah terakhir dalam persiapan data adalah membagi dataset menjadi data latih (training set) dan data uji (testing set). Ini dilakukan untuk mengevaluasi kinerja model pada data yang belum pernah dilihat oleh model selama pelatihan.
     ```
     from sklearn.model_selection import train_test_split

     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

     ```
    Pembagian data ini penting untuk mengukur seberapa baik model dapat melakukan generalisasi pada data baru. Data uji akan digunakan untuk mengevaluasi performa model yang telah dilatih pada data latih.

## Modeling

Pada tahap ini, model **Linear Support Vector Classifier (LinearSVC)** digunakan untuk menyelesaikan masalah klasifikasi sentimen pada tweet. LinearSVC dipilih karena lebih efisien dalam menangani dataset besar dengan banyak fitur, terutama saat menggunakan representasi teks berbasis **TF-IDF**. Pemodelan dilakukan melalui dua tahapan: **pembuatan model dasar (baseline model)** dan **peningkatan kinerja melalui hyperparameter tuning**.

### 1. Linear Support Vector Classifier (LinearSVC)
LinearSVC adalah versi yang dioptimalkan dari **Support Vector Machines (SVM)** yang bekerja dengan asumsi data dapat dipisahkan secara linier. Algoritma ini bertujuan untuk menemukan garis atau hyperplane terbaik yang memisahkan data ke dalam kelas-kelas yang berbeda dengan margin terbesar.

#### Kelebihan LinearSVC:
- **Efisiensi dalam skala besar**: LinearSVC sangat cepat dan efisien untuk dataset besar dengan banyak fitur, seperti representasi teks berbasis **TF-IDF**.
- **Tidak memerlukan kernel**: LinearSVC bekerja langsung dengan fitur linier, tanpa menggunakan kernel seperti SVM tradisional, sehingga lebih sederhana dan efisien dari segi komputasi.
- **Kemampuan regulasi**: Parameter regulasi (**C**) dapat diatur untuk menyesuaikan kompleksitas model, membantu dalam menghindari **overfitting**.

#### Kekurangan LinearSVC:
- **Kurang fleksibel untuk data yang tidak linier**: LinearSVC tidak dapat menangani data yang tidak dapat dipisahkan secara linier dengan baik, berbeda dengan SVM dengan kernel non-linier seperti **RBF**.
- **Kurang sensitif terhadap data yang kompleks**: LinearSVC mungkin tidak memberikan performa optimal jika data memerlukan transformasi non-linier untuk dipisahkan dengan baik.

### 2. Baseline Model
Sebagai langkah pertama, model dasar dibangun menggunakan **LinearSVC** dengan parameter default. Model dievaluasi menggunakan metrik **precision**, **recall**, dan **F1-score** untuk setiap kelas sentimen (positive, neutral, dan negative). Hasil dari baseline model ini menjadi titik awal untuk peningkatan kinerja model.

### 3. Hyperparameter Tuning
Setelah membangun model dasar, langkah berikutnya adalah meningkatkan kinerja model melalui **hyperparameter tuning**. Parameter utama yang disesuaikan adalah:

- **C**: Mengontrol keseimbangan antara margin besar dan kesalahan klasifikasi.
- **penalty**: Jenis regulasi yang digunakan (hanya **l2** yang valid untuk **dual=True**).
- **loss**: Fungsi kerugian yang digunakan untuk mengoptimalkan model, seperti **hinge** atau **squared_hinge**.
- **max_iter**: Jumlah iterasi maksimum yang diizinkan untuk algoritma konvergen.

#### Proses Improvement:
- **Tuning Parameter C**: Nilai **C** yang lebih kecil mendorong model untuk memiliki margin lebih luas, menghindari overfitting, sementara nilai yang lebih tinggi memberikan performa lebih baik pada data latih tetapi berisiko **overfitting**.
- **Pemilihan Loss**: Fungsi kerugian **hinge** lebih sederhana tetapi **squared_hinge** sering kali memberikan performa yang lebih stabil.
- **Tuning max_iter**: Jumlah iterasi yang cukup tinggi diperlukan untuk memastikan konvergensi model, terutama pada dataset besar.

### 4. Best Parameters
Hasil tuning menghasilkan parameter terbaik sebagai berikut:
- **C**: 1
- **penalty**: l2
- **loss**: hinge
- **max_iter**: 5000

Hyperparameter tuning dilakukan untuk memaksimalkan performa model tanpa overfitting, namun hasil evaluasi menunjukkan bahwa peningkatan performa dari baseline model tidak signifikan.

> Penjelasan performa model akan dibahas lebih lanjut pada bagian **Evaluation**.

---


## **Evaluation**

Pada bagian ini, model **LinearSVC** dievaluasi menggunakan beberapa metrik untuk mengukur performanya dalam mengklasifikasikan sentimen tweet. Metrik yang digunakan dalam evaluasi ini adalah **precision**, **recall**, dan **F1-score**, yang memberikan pandangan komprehensif tentang kinerja model, khususnya dalam tugas klasifikasi multikelas. Metrik-metrik ini dipilih karena cocok untuk masalah klasifikasi yang melibatkan ketidakseimbangan kelas, seperti klasifikasi sentimen.

#### **Penjelasan Metrik yang Digunakan**

1. **Precision**:
   - **Definisi**: Precision mengukur seberapa banyak prediksi positif yang benar-benar positif. Artinya, precision menghitung seberapa akurat model ketika memprediksi sebuah kelas tertentu.
   - **Formula**:
     
     $$\text{Precision} = \frac{TP}{TP + FP}$$
     
     Di mana **TP** (True Positive) adalah jumlah prediksi benar untuk kelas positif, dan **FP** (False Positive) adalah jumlah prediksi salah untuk kelas positif.
   - **Kegunaan**: Precision penting saat false positive lebih kritis, seperti dalam konteks deteksi spam atau konten negatif, di mana salah deteksi bisa berdampak besar.

2. **Recall**:
   - **Definisi**: Recall mengukur seberapa baik model menangkap semua kasus positif yang sebenarnya ada. Ini menunjukkan kemampuan model untuk menemukan semua instance dari kelas tertentu.
   - **Formula**:
     
     $$\text{Recall} = \frac{TP}{TP + FN}$$
     
     Di mana **FN** (False Negative) adalah jumlah prediksi salah untuk kelas negatif.
   - **Kegunaan**: Recall sangat penting ketika kita tidak ingin melewatkan instance positif, misalnya dalam kasus di mana pendeteksian sentimen negatif sangat penting.

3. **F1-score**:
   - **Definisi**: F1-score adalah harmonic mean dari precision dan recall. F1-score memberikan keseimbangan antara precision dan recall, yang sangat bermanfaat saat kedua metrik tersebut sama pentingnya.
   - **Formula**:
     
     $$\text{F1-score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
     
   - **Kegunaan**: F1-score memberikan pandangan keseluruhan performa model, terutama saat ada ketidakseimbangan antara precision dan recall.

---

Setelah melakukan pemodelan dengan **Linear Support Vector Classifier (LinearSVC)**, evaluasi dilakukan dalam dua tahap: **baseline model** dengan parameter default, dan model yang telah mengalami **hyperparameter tuning**. Metrik evaluasi yang digunakan untuk mengukur kinerja model adalah **precision**, **recall**, **F1-score**, dan **accuracy**.

#### 1. Baseline Model
Pada baseline, model LinearSVC dijalankan dengan parameter default tanpa penyesuaian lebih lanjut. Hasil evaluasi baseline model:

| **Class**  | **Precision** | **Recall** | **F1-Score** | **Support** |
|------------|---------------|------------|--------------|-------------|
| Negative   | 0.97          | 0.97       | 0.97         | 47,674      |
| Neutral    | 0.96          | 0.96       | 0.96         | 38,723      |
| Positive   | 0.98          | 0.97       | 0.98         | 47,688      |

- **Accuracy**: 97%
- **Macro Avg**: Precision (0.97), Recall (0.97), F1-Score (0.97)
- **Weighted Avg**: Precision (0.97), Recall (0.97), F1-Score (0.97)

#### 2. Model with Hyperparameter Tuning
Setelah baseline, dilakukan hyperparameter tuning untuk memaksimalkan performa model. Proses tuning melibatkan penyesuaian parameter seperti:

- **C**: Parameter regulasi untuk mengontrol margin.
- **Penalty**: Penggunaan penalti L2 untuk menghindari overfitting.
- **Max Iter**: Jumlah iterasi maksimum untuk mencapai konvergensi.

Hasil dari model yang telah di-tuning:

| **Class**  | **Precision** | **Recall** | **F1-Score** | **Support** |
|------------|---------------|------------|--------------|-------------|
| Negative   | 0.97          | 0.97       | 0.97         | 47,674      |
| Neutral    | 0.96          | 0.96       | 0.96         | 38,723      |
| Positive   | 0.98          | 0.97       | 0.98         | 47,688      |

- **Accuracy**: 97%
- **Macro Avg**: Precision (0.97), Recall (0.97), F1-Score (0.97)
- **Weighted Avg**: Precision (0.97), Recall (0.97), F1-Score (0.97)

#### 3. Comparative Analysis
Dari hasil evaluasi, baik **baseline model** maupun **model yang telah di-tuning** menunjukkan performa yang hampir identik. Tidak ada perbedaan signifikan dalam metrik evaluasi utama seperti precision, recall, F1-score, atau accuracy. Hal ini menunjukkan bahwa **baseline model sudah optimal** dan tidak mengalami overfitting atau underfitting pada dataset yang digunakan.

#### 4. Model Terbaik
Karena tidak ada peningkatan signifikan dari hyperparameter tuning, **baseline model** dipilih sebagai model terbaik. Alasan pemilihan baseline model adalah:

- Sudah memberikan kinerja yang sangat baik dengan accuracy dan F1-score di atas 97%.
- Tidak memerlukan tuning lebih lanjut, yang menghemat waktu dan sumber daya.
- Sederhana dan lebih efisien tanpa tambahan kompleksitas yang tidak diperlukan.

---



### **Evaluasi Terhadap Problem Statements**

1. **Pernyataan Masalah 1: Penyebaran Konten Negatif di Twitter**
   - **Hasil Model**: Model klasifikasi sentimen yang dikembangkan menggunakan **LinearSVC** dengan teknik **TF-IDF** menunjukkan akurasi yang sangat tinggi (97% di seluruh metrik evaluasi utama, seperti precision, recall, dan F1-score). Hal ini menunjukkan bahwa model mampu mendeteksi tweet dengan sentimen negatif secara efektif.
   - **Dampak Terhadap Bisnis**: Model ini dapat diterapkan di Twitter untuk secara otomatis mendeteksi dan memblokir tweet yang mengandung konten negatif. Dengan tingkat akurasi yang tinggi, penyebaran konten negatif akan berkurang secara signifikan, membantu menjaga keamanan dan kenyamanan pengguna Twitter.
   
2. **Pernyataan Masalah 2: Ketidakmampuan Pendekatan Manual dalam Memfilter Konten**
   - **Hasil Model**: Implementasi model machine learning berbasis **LinearSVC** menggantikan pendekatan manual dalam memoderasi konten. Dengan kemampuan memproses ribuan tweet secara cepat dan real-time, model ini memberikan solusi otomatis yang efektif.
   - **Dampak Terhadap Bisnis**: Pendekatan otomatis yang lebih efektif ini akan menghemat waktu dan sumber daya, sehingga meningkatkan efisiensi moderasi konten di Twitter, terutama mengingat volume besar tweet yang diposting setiap hari.

3. **Pernyataan Masalah 3: Keterbatasan Algoritma dalam Mengenali Nuansa Bahasa**
   - **Hasil Model**: Dengan pendekatan **TF-IDF**, model ini dapat mengenali konteks dan nuansa dalam tweet, bukan hanya kata-kata kasar eksplisit. Ini memungkinkan model untuk mendeteksi tweet negatif yang ditulis dengan bahasa yang lebih halus atau tidak langsung.
   - **Dampak Terhadap Bisnis**: Peningkatan kemampuan untuk mengenali konteks dan nuansa dalam teks akan membuat Twitter lebih efisien dalam memblokir tweet berbahaya yang sulit dideteksi oleh algoritma moderasi konvensional.

---

### **Apakah Goals Sudah Dicapai?**

1. **Jawaban Pernyataan Masalah 1**:
   - **Mengurangi Penyebaran Konten Negatif di Twitter**: Dengan model yang mampu mencapai **F1-score** sebesar 0.97 untuk tweet negatif, model ini telah secara efektif memenuhi tujuan untuk mendeteksi dan memblokir konten negatif.
   
2. **Jawaban Pernyataan Masalah 2**:
   - **Meningkatkan Efektivitas Moderasi Konten**: Implementasi model machine learning telah menggantikan pendekatan manual dan memungkinkan moderasi otomatis dalam skala besar. Hal ini akan meningkatkan efektivitas dalam memoderasi konten negatif secara real-time.

3. **Jawaban Pernyataan Masalah 3**:
   - **Meningkatkan Akurasi Pendeteksian Konten Negatif**: Dengan kemampuan model untuk mengenali konteks dan nuansa bahasa menggunakan TF-IDF, akurasi dalam mendeteksi tweet negatif telah meningkat, bahkan untuk tweet yang tidak secara eksplisit menggunakan kata-kata kasar.

---

### **Dampak dari Solution Statements**

1. **Solution Statement 1: Penggunaan LinearSVC dengan Teknik TF-IDF**
   - **Dampak**: LinearSVC, dengan kombinasi teknik feature engineering TF-IDF, memberikan hasil yang optimal dalam menangani masalah klasifikasi teks besar dan beragam tweet. Model ini mampu memisahkan tweet dengan sentimen negatif dari yang lain dengan akurasi yang sangat tinggi, memenuhi harapan bisnis untuk mengurangi penyebaran konten negatif di Twitter.
   
2. **Solution Statement 2: Hyperparameter Tuning**
   - **Dampak**: Meskipun tuning dilakukan, hasilnya menunjukkan bahwa performa model baseline sudah sangat optimal. Ini menegaskan bahwa solusi yang diberikan oleh model baseline sudah cukup efisien tanpa memerlukan banyak penyesuaian tambahan. Hal ini memastikan bahwa solusi bisa diimplementasikan dengan cepat tanpa memerlukan kompleksitas tambahan dalam proses pengaturan model.

---

### **Kesimpulan**

Berdasarkan hasil evaluasi, model yang dikembangkan menggunakan LinearSVC dan TF-IDF berhasil menjawab seluruh pernyataan masalah serta mencapai semua tujuan yang telah ditetapkan. Model ini mampu mengidentifikasi sentimen publik terhadap suatu topik secara otomatis dan akurat, khususnya dalam kasus seperti pemilu atau kebijakan pemerintah.

Model ini memberikan solusi yang signifikan untuk memudahkan analisis sentimen di media sosial, menggantikan pendekatan manual yang tidak efisien. Dengan evaluasi metrik yang mencapai akurasi, precision, dan recall yang tinggi, model ini mampu mendeteksi dan mengklasifikasikan tweet negatif, netral, maupun positif dengan baik. Pendekatan ini sangat berguna dalam membantu pihak terkait, seperti lembaga penelitian atau pengambil kebijakan, untuk memahami persepsi publik secara lebih cepat dan tepat.

Secara keseluruhan, penerapan LinearSVC dan TF-IDF memberikan hasil yang memadai dalam membangun sistem klasifikasi sentimen yang efektif untuk berbagai topik diskusi di Twitter, meningkatkan kemampuan untuk menganalisis sentimen publik dalam skala besar dengan nuansa bahasa yang beragam.




