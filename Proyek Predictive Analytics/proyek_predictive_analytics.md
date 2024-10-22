# Laporan Proyek Machine Learning - Muhammad Reza Ubaidillah

## Latar Belakang

Dengan perkembangan industri wine yang semakin pesat dan permintaan global yang meningkat, standar kualitas wine menjadi aspek penting yang menentukan daya saing di pasar internasional. Namun, penilaian kualitas yang dilakukan secara manual oleh pakar wine memakan waktu dan biaya yang tidak sedikit, selain cenderung subjektif.

Dengan adanya dataset *wine quality*, yang mencakup pengukuran berbagai parameter kimia dalam wine, seperti keasaman tetap, keasaman volatil, kandungan alkohol, dan gula residu, proyek ini bertujuan untuk membangun model machine learning yang mampu memprediksi kualitas wine secara otomatis. Penggunaan machine learning dapat mempercepat proses evaluasi, mengurangi biaya, dan memberikan hasil yang lebih objektif dan konsisten.

### Masalah yang Diselesaikan

Masalah utama yang ingin diselesaikan adalah mengotomatisasi proses penilaian kualitas wine berdasarkan parameter kimia yang terukur secara objektif. Dengan demikian, subjektivitas dalam evaluasi kualitas dapat dikurangi, dan keputusan yang lebih data-driven dapat diambil dalam proses produksi wine. Selain itu, proyek ini juga diharapkan dapat membantu para produsen wine untuk memahami faktor-faktor kimia yang paling berpengaruh terhadap kualitas wine.

Teknologi machine learning, seperti Support Vector Machine (SVM) dan Random Forest, telah terbukti efektif dalam menyelesaikan masalah klasifikasi seperti ini, di mana fitur input digunakan untuk memprediksi label kelas (kualitas wine). Penelitian terdahulu menunjukkan bahwa teknik ini mampu meningkatkan akurasi prediksi dibandingkan dengan metode tradisional.

### Referensi

Supriyadi, Riki, et al. "Penerapan Algoritma Random Forest Untuk Menentukan Kualitas Anggur Merah." *E-Bisnis: Jurnal Ilmiah Ekonomi Dan Bisnis* 13.2 (2020): 67-75.

## Business Understanding

### Problem Statements

Berdasarkan analisis awal terhadap dataset *wine quality*, beberapa masalah utama yang dihadapi industri wine terkait dengan kualitas produk adalah sebagai berikut:

#### Pernyataan Masalah 1
Proses penilaian kualitas wine yang dilakukan secara manual membutuhkan waktu yang lama dan dapat bersifat subjektif, sehingga menghasilkan evaluasi yang bervariasi tergantung pada siapa yang menilai.

#### Pernyataan Masalah 2
Produsen wine memerlukan alat prediksi yang dapat mengidentifikasi faktor-faktor kimia yang memengaruhi kualitas wine secara konsisten dan dapat diukur secara objektif, sehingga membantu mereka dalam meningkatkan kontrol kualitas produk.

#### Pernyataan Masalah 3
Dengan banyaknya variabel kimia yang mempengaruhi kualitas wine, sulit untuk secara manual menentukan kombinasi yang paling signifikan. Ini menimbulkan tantangan dalam upaya optimasi produksi untuk menjaga kualitas terbaik.

### Goals

Berdasarkan masalah-masalah di atas, tujuan dari proyek ini adalah:

#### Jawaban Pernyataan Masalah 1
Mengembangkan model machine learning yang mampu memprediksi kualitas wine secara otomatis, menggantikan penilaian manual yang rentan terhadap subjektivitas, sehingga menghasilkan penilaian yang lebih cepat dan konsisten.

#### Jawaban Pernyataan Masalah 2
Mengidentifikasi fitur kimia yang paling signifikan dalam mempengaruhi kualitas wine, dengan memanfaatkan metode machine learning untuk membantu produsen wine dalam mengoptimalkan proses produksi dan kontrol kualitas.

#### Jawaban Pernyataan Masalah 3
Membangun model prediktif yang dapat mengevaluasi secara cepat faktor-faktor mana yang paling berpengaruh, sekaligus memberikan rekomendasi bagi produsen dalam meningkatkan proses produksi berdasarkan data kimia yang tersedia.

### Solution Statements

Untuk mencapai tujuan di atas, beberapa solusi yang akan diterapkan dalam proyek ini adalah:

#### Solution Statement 1
Menggunakan beberapa algoritma machine learning untuk membandingkan performa prediksi kualitas wine, seperti **Random Forest** dan **Support Vector Machine (SVM)**. Kedua model ini dipilih karena kemampuannya dalam menangani data klasifikasi dan menangkap interaksi kompleks antar fitur.

#### Solution Statement 2
Melakukan **hyperparameter tuning** untuk meningkatkan performa baseline model, baik untuk Random Forest maupun SVM. Hyperparameter tuning akan dilakukan dengan metode grid search atau random search untuk mencari kombinasi parameter yang optimal guna meningkatkan akurasi prediksi.

#### Solution Statement 3
Mengukur performa model menggunakan metrik evaluasi yang tepat, seperti **akurasi**, **precision**, **recall**, dan **F1-score**, guna memastikan bahwa model yang dihasilkan tidak hanya akurat dalam prediksi, tetapi juga mampu menangani kesalahan prediksi dengan seimbang.

Dengan menggunakan algoritma yang tepat serta tuning hyperparameter, solusi yang diusulkan diharapkan mampu menghasilkan model prediksi yang akurat dan dapat diimplementasikan dalam proses produksi wine untuk meningkatkan konsistensi dan kualitas produk.
