# Laporan Proyek Machine Learning - Muhammad Reza Ubaidillah
Di era digital saat ini, media sosial telah menjadi bagian dari kehidupan sehari-hari masyarakat dunia. Twitter, salah satu platform media sosial yang terkemuka, memungkinkan pengguna untuk berbagi opini, pengalaman, dan informasi melalui pesan singkat yang disebut "tweet". Namun, karena kebebasan berpendapat yang diberikan, platform ini juga rentan terhadap penyebaran konten negatif seperti ujaran kebencian, kekerasan verbal, dan pesan berisi provokasi. Fenomena ini memunculkan kebutuhan mendesak untuk solusi yang efektif guna melindungi pengguna dari dampak buruk konten semacam itu.

Twitter sendiri telah mengambil beberapa langkah untuk menangani masalah ini, namun pendekatan manual dan otomatis yang ada belum sepenuhnya efektif. Salah satu cara untuk mengatasi tantangan ini adalah dengan memanfaatkan teknologi kecerdasan buatan, khususnya Natural Language Processing (NLP), untuk mengembangkan model klasifikasi sentimen yang dapat mengidentifikasi tweet negatif dan secara otomatis mengambil tindakan terhadap konten tersebut. Dengan menganalisis sentimen tweet, Twitter dapat secara proaktif meminimalkan konten yang merusak dan menciptakan lingkungan online yang lebih sehat.

- **Mengapa dan Bagaimana Masalah Ini Harus Diselesaikan**
Masalah konten negatif di media sosial, termasuk Twitter, memiliki dampak luas pada pengalaman pengguna. Ujaran kebencian dan konten ofensif dapat memicu konflik sosial, merusak reputasi platform, serta mengganggu kesehatan mental para pengguna. Meningkatnya jumlah pengguna media sosial setiap hari membuat pengawasan manual terhadap semua konten menjadi tidak mungkin dilakukan. Oleh karena itu, solusi berbasis machine learning, seperti analisis sentimen, menjadi penting dalam mengelola volume besar data yang dihasilkan oleh pengguna.
Model analisis sentimen berbasis NLP memungkinkan platform untuk mengenali emosi atau sentimen yang terkandung dalam teks, yang kemudian dikategorikan sebagai sentimen positif, netral, atau negatif. Melalui penerapan model ini, Twitter dapat lebih cepat mendeteksi dan memblokir konten berbahaya sebelum beredar luas. Implementasi solusi ini dapat meningkatkan pengalaman pengguna, menjaga komunitas tetap aman, serta memperkuat citra positif platform.

- Referensi: 
Fani, Syiva Multi, Rukun Santoso, and Suparti Suparti. "Penerapan Text Mining Untuk Melakukan Clustering Data Tweet Akun Blibli Pada Media Sosial Twitter Menggunakan K-Means Clustering." Jurnal Gaussian 10.4 (2021): 583-593.
  

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
    - Support: Mengindikasikan jumlah data aktual di setiap kategori (negatif, positif, dll) yang digunakan untuk menghitung precision dan recall.
    
    Dengan pendekatan ini, kita dapat memastikan bahwa model yang dibangun fokus pada akurasi dalam mendeteksi tweet negatif tanpa mengabaikan konteks penting yang relevan.

## Data Understanding
Dalam proyek ini, data yang digunakan berasal dari dataset Twitter Sentiment Analysis yang tersedia di Kaggle. Dataset ini berisi tweet yang telah diberi label sentimen. Dataset dapat diakses melalui tautan berikut: [Twitter Sentiment Analysis Dataset.](https://www.kaggle.com/datasets/daniel09817/twitter-sentiment-analysis)

Dataset ini dirancang untuk tugas klasifikasi sentimen, di mana setiap tweet dikategorikan ke dalam tiga jenis sentimen: positif, negatif, atau other. Data ini akan digunakan untuk melatih model  Linear Support Vector Classifier (LinearSVC) dalam mendeteksi sentimen tweet secara otomatis.


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

## Modeling
Pada tahap ini, model Linear Support Vector Classifier (LinearSVC) digunakan untuk menyelesaikan masalah klasifikasi sentimen pada tweet. LinearSVC dipilih karena lebih efisien dalam menangani dataset besar dengan banyak fitur, terutama saat menggunakan representasi teks berbasis TF-IDF. Pemodelan dilakukan melalui dua tahapan: pembuatan model dasar (baseline model) dan peningkatan kinerja melalui hyperparameter tuning.

- . Linear Support Vector Classifier (LinearSVC)
LinearSVC adalah versi yang dioptimalkan dari Support Vector Machines (SVM) yang bekerja dengan asumsi data dapat dipisahkan secara linier. Algoritma ini bertujuan untuk menemukan garis atau hyperplane terbaik yang memisahkan data ke dalam kelas-kelas yang berbeda dengan margin terbesar.
    
    Kelebihan LinearSVC:
    - Efisiensi dalam skala besar: LinearSVC sangat cepat dan efisien untuk dataset yang besar dengan banyak fitur, seperti representasi teks berbasis TF-IDF.
    - Tidak memerlukan kernel: Tidak seperti SVM tradisional yang menggunakan kernel, LinearSVC bekerja langsung dengan fitur linier, sehingga lebih sederhana dan efisien dari segi komputasi.
    - Kemampuan regulasi: Parameter regulasi (C) dapat diatur untuk menyesuaikan kompleksitas model, membantu dalam menghindari overfitting.

    Kekurangan LinearSVC:
    - Kurang fleksibel untuk data yang tidak dapat dipisahkan secara linier: LinearSVC tidak dapat menangani data yang tidak linier dengan baik, berbeda dengan SVM dengan kernel non-linier seperti RBF.
    - Kurang sensitif terhadap data yang memiliki kompleksitas non-linier: Jika data memerlukan transformasi non-linier untuk dipisahkan dengan baik, LinearSVC mungkin tidak akan memberikan performa optimal.
- . Baseline Model
Sebagai langkah pertama, Model dasar dibangun menggunakan LinearSVC dengan parameter default. Ini memberikan gambaran awal tentang performa model tanpa penyesuaian lebih lanjut.
    ```
    from sklearn.svm import LinearSVC
    from sklearn.metrics import classification_report
    
    # Membuat model SVM dasar
    svm_model = LinearSVC()  # Menggunakan parameter default
    svm_model.fit(X_train, y_train)
    
    # Evaluasi model pada data uji
    y_pred = svm_model.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    ```

     Model dievaluasi menggunakan metrik precision, recall, F1-score, dan support untuk setiap kelas sentimen (positif, negatif, dan other). Hasil dari model baseline ini menjadi titik awal untuk meningkatkan kinerja model.
     Hasil evaluasi untuk model baseline LinearSVC tanpa hyperparameter tuning menunjukkan performa yang sangat baik dengan metrik berikut:
     |              | precision | recall | f1-score | support |
    |--------------|-----------|--------|----------|---------|
    | negative     | 0.97      | 0.97   | 0,97     | 47674   |
    | neutral      | 0.96      | 0.96   | 0.96     | 38723   |
    | positive     | 0.98      | 0.97   | 0.98     | 47688   |
    | accuracy     |           |        | 0.97     | 134085  |
    | macro avg    | 0.97      | 0.97   | 0.97     | 134085  |
    | weighted avg | 0.97      | 0.97   | 0.97     | 134085  |
    Model baseline sudah menunjukkan performa yang sangat baik dengan F1-score yang konsisten di semua kelas. Namun, untuk memastikan model ini mencapai hasil optimal, dilakukan hyperparameter tuning.
- . Hyperparameter Tuning
Setelah membuat model dasar, langkah berikutnya adalah meningkatkan kinerja model dengan melakukan hyperparameter tuning. Parameter utama yang disesuaikan adalah:

    - C: Parameter regulasi yang mengontrol keseimbangan antara margin besar dan kesalahan klasifikasi. Nilai C yang lebih tinggi mengurangi margin tetapi bisa menyebabkan overfitting.
    - penalty: Menentukan jenis regulasi yang digunakan. Pada LinearSVC, hanya l2 yang valid untuk dual=True.
    - loss: Fungsi kerugian yang digunakan untuk mengoptimalkan model, seperti hinge atau squared_hinge.
    - max_iter: Jumlah iterasi maksimum yang diizinkan untuk algoritma konvergen.
    
    ```
   from sklearn.model_selection import GridSearchCV

    # Definisikan parameter untuk GridSearch
    param_grid = {
        'C': [0.1, 1, 10, 100],
        'penalty': ['l2'],
        'loss': ['hinge', 'squared_hinge'],
        'max_iter': [1000, 2000, 5000]
    }
    
    # Membangun model dengan GridSearchCV
    grid_search = GridSearchCV(LinearSVC(), param_grid, refit=True, verbose=2, cv=5)
    grid_search.fit(X_train, y_train)
    
    # Hasil parameter terbaik
    print("Best Parameters: ", grid_search.best_params_)
    
    # Evaluasi model yang di-tune pada data uji
    y_pred_tuned = grid_search.best_estimator_.predict(X_test)
    print(classification_report(y_test, y_pred_tuned))
    ```
    Proses Improvement:
    - Tuning Parameter C: Nilai C yang lebih kecil (0.1) mendorong model untuk memiliki margin lebih luas, menghindari overfitting, sedangkan nilai yang lebih tinggi (100) dapat memberikan performa lebih baik pada data latih tetapi berisiko overfitting.
    - Pemilihan Loss: Fungsi kerugian hinge mungkin lebih sederhana tetapi squared_hinge sering kali memberikan performa lebih stabil.
    - Tuning max_iter: Jumlah iterasi yang cukup tinggi diperlukan untuk memastikan konvergensi model, terutama pada dataset besar.
    
    Setelah dilakukan hyperparameter tuning, hasil evaluasi menunjukkan bahwa tidak ada perubahan signifikan dalam performa model:
    |              | precision | recall | f1-score | support |
    |--------------|-----------|--------|----------|---------|
    | negative     | 0.97      | 0.97   | 0,97     | 47674   |
    | neutral      | 0.96      | 0.96   | 0.96     | 38723   |
    | positive     | 0.98      | 0.97   | 0.98     | 47688   |
    | accuracy     |           |        | 0.97     | 134085  |
    | macro avg    | 0.97      | 0.97   | 0.97     | 134085  |
    | weighted avg | 0.97      | 0.97   | 0.97     | 134085  |
    
    Setelah melakukan hyperparameter tuning, tidak terjadi peningkatan yang signifikan dari performa model baseline. Model LinearSVC yang sudah menggunakan parameter default memberikan hasil yang optimal sejak awal, dengan precision, recall, dan F1-score yang tinggi di seluruh kelas sentimen. Tuning parameter, meskipun sudah diterapkan dengan variasi yang cukup luas, tidak memberikan peningkatan berarti.

Ini menunjukkan bahwa model LinearSVC dengan TF-IDF telah memberikan generalisasi yang sangat baik pada dataset ini tanpa memerlukan banyak penyesuaian parameter tambahan.

### **Evaluation**

Pada bagian ini, model **LinearSVC** dievaluasi menggunakan beberapa metrik untuk mengukur performanya dalam mengklasifikasikan sentimen tweet. Metrik yang digunakan dalam evaluasi ini adalah **precision**, **recall**, **F1-score**, dan **support**, yang memberikan pandangan komprehensif tentang kinerja model, khususnya dalam tugas klasifikasi multikelas. Metrik-metrik ini dipilih karena cocok untuk masalah klasifikasi yang melibatkan ketidakseimbangan kelas, seperti klasifikasi sentimen.

#### **Penjelasan Metrik yang Digunakan**

1. **Precision**:
   - **Definisi**: Precision mengukur seberapa banyak prediksi positif yang benar-benar positif. Artinya, precision menghitung seberapa akurat model ketika memprediksi sebuah kelas tertentu.
   - **Formula**: 
        $$$
         \text{Precision} = \frac{TP}{TP + FP}
        $$$

     Di mana **TP** (True Positive) adalah jumlah prediksi benar untuk kelas positif, dan **FP** (False Positive) adalah jumlah prediksi salah untuk kelas positif.
   - **Kegunaan**: Precision penting saat false positive lebih kritis, seperti dalam konteks deteksi spam atau konten negatif, di mana salah deteksi bisa berdampak besar.

2. **Recall**:
   - **Definisi**: Recall mengukur seberapa baik model menangkap semua kasus positif yang sebenarnya ada. Ini menunjukkan kemampuan model untuk menemukan semua instance dari kelas tertentu.
   - **Formula**:
     $$$
     \text{Recall} = \frac{TP}{TP + FN}
     $$$

     Di mana **FN** (False Negative) adalah jumlah prediksi salah untuk kelas negatif.
   - **Kegunaan**: Recall sangat penting ketika kita tidak ingin melewatkan instance positif, misalnya dalam kasus di mana pendeteksian sentimen negatif sangat penting.

3. **F1-score**:
   - **Definisi**: F1-score adalah harmonic mean dari precision dan recall. F1-score memberikan keseimbangan antara precision dan recall, yang sangat bermanfaat saat kedua metrik tersebut sama pentingnya.
   - **Formula**:
     $$$
     \text{F1-score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
     $$$

   - **Kegunaan**: F1-score memberikan pandangan keseluruhan performa model, terutama saat ada ketidakseimbangan antara precision dan recall.

4. **Support**:
   - **Definisi**: Support adalah jumlah instance sebenarnya dari setiap kelas dalam dataset. Ini menunjukkan seberapa besar atau kecil tiap kelas dibandingkan dengan yang lain.
   - **Kegunaan**: Support membantu kita melihat distribusi data di tiap kelas dan bagaimana model menangani kelas yang mungkin lebih jarang muncul.



### **Hasil Evaluasi Berdasarkan Metrik yang Digunakan**

Berdasarkan evaluasi menggunakan metrik **precision**, **recall**, dan **F1-score**, hasilnya adalah sebagai berikut:

| **Sentimen**  | **Precision** | **Recall** | **F1-score** | **Support** |
|---------------|---------------|------------|--------------|-------------|
| Negative      | 0.97          | 0.97       | 0.97         | 47,674      |
| Neutral       | 0.96          | 0.96       | 0.96         | 38,723      |
| Positive      | 0.98          | 0.97       | 0.98         | 47,688      |
| **Accuracy**  | **0.97**      | -          | -            | 134,085     |
| **Macro avg** | 0.97          | 0.97       | 0.97         | 134,085     |
| **Weighted avg** | 0.97       | 0.97       | 0.97         | 134,085     |

#### **Analisis Hasil**:

1. **Precision**: Semua kelas (negative, neutral, dan positive) memiliki precision di atas 0.96, menunjukkan bahwa model mampu memprediksi dengan tingkat akurasi yang tinggi untuk setiap kelas. Precision yang tinggi mengindikasikan bahwa jumlah false positive relatif rendah, sehingga model jarang salah dalam mengklasifikasikan sentimen tweet.
   
2. **Recall**: Recall untuk semua kelas juga sangat tinggi (0.96-0.97), yang menunjukkan bahwa model mampu menemukan hampir semua instance dari setiap kelas. Ini sangat penting dalam konteks analisis sentimen, terutama untuk mendeteksi konten negatif.

3. **F1-score**: Dengan nilai F1-score rata-rata di atas 0.97, model memberikan keseimbangan yang baik antara precision dan recall. F1-score yang tinggi memastikan bahwa model tidak hanya akurat tetapi juga efektif dalam menangkap seluruh variasi sentimen di dalam dataset.

4. **Akurasi**: Akurasi keseluruhan model adalah 0.97, yang menunjukkan bahwa 97% dari prediksi model sesuai dengan label sebenarnya pada data uji. Ini adalah akurasi yang sangat baik untuk masalah klasifikasi dengan tiga kelas sentimen.

---

### **Kesimpulan**

Evaluasi model dengan menggunakan metrik precision, recall, F1-score, dan support menunjukkan bahwa **LinearSVC** memberikan performa yang sangat baik dalam mengklasifikasikan sentimen tweet. Metrik-metrik ini memberikan gambaran menyeluruh tentang kemampuan model dalam menangani data teks dan memastikan model bekerja secara optimal dalam mendeteksi berbagai jenis sentimen tanpa bias yang berarti.


