# -*- coding: utf-8 -*-
"""twitter-sentiment-analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SrBD0njBVjv7Mw4IdK3mzCXguL8xgfxd

## Data *Gathering*

mengumpulkan dataset dari kaggle https://www.kaggle.com/datasets/daniel09817/twitter-sentiment-analysis
"""

!kaggle datasets download -d daniel09817/twitter-sentiment-analysis

!unzip twitter-sentiment-analysis.zip

"""### Import Semua Liblaries Yang Digunakan

mengimport semua liblares yang digunakan dalam notebook ini
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

"""## Accessing data

menampilkan 5 data teratas
"""

df = pd.read_csv('/content/twitter sentiment analysis.csv')
df.head()

"""Menampilkan informasi dataset"""

df.info()

"""###Data Cleaning

menampilkan data yang memiliki nilai kosong pada masing - masing label
"""

df.isnull().sum()

"""menghapus nilai kosong pada dataset"""

df.dropna(inplace=True)

"""menjumlahkan isi baris yang duplicate pada kolom text"""

df.duplicated(subset='Text').sum()

"""menghapus semua isi baris yang duplicate pada kolom text"""

df.drop_duplicates(subset='Text',inplace=True)

"""deskripi statistik pada data"""

df.describe()

"""### EDA

memvisualisasi distribusi sentimen positif, negatif dan netral pada bar chart
"""

sns.countplot(x='Label', data=df)
plt.title('Distribusi Sentimen')
plt.show()

"""memvisualisasi distribusi frekuensi jumlah kata menggunakan histogram"""

df['tweet_length'] = df['Text'].apply(lambda x: len(x.split()))  # Hitung jumlah kata
sns.histplot(df['tweet_length'], bins=30, kde=True)
plt.title('Distribusi Panjang Tweet')
plt.xlabel('Jumlah Kata')
plt.ylabel('Frekuensi')
plt.show()

"""memvisualisasi kata kata yang paling sering muncul dalam label positif menggunakan wordcloud"""

# Word Cloud untuk sentimen positif
positive_tweets = ' '.join(df[df['Label'] == 'positive']['Text'])
wordcloud = WordCloud(width=800, height=400, max_words=100, background_color='white').generate(positive_tweets)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud - Sentimen Positif')
plt.show()

"""memvisualisasi kata kata yang paling sering muncul dalam label negatif menggunakan wordcloud"""

# Word Cloud untuk sentimen negatif
negative_tweets = ' '.join(df[df['Label'] == 'negative']['Text'])
wordcloud = WordCloud(width=800, height=400, max_words=100, background_color='white').generate(negative_tweets)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud - Sentimen Negatif')
plt.show()

"""memvisualisasi kata kata yang paling sering muncul dalam label neutral menggunakan wordcloud"""

# Word Cloud untuk sentimen neutral
neutral_tweets = ' '.join(df[df['Label'] == 'neutral']['Text'])
wordcloud = WordCloud(width=800, height=400, max_words=100, background_color='white').generate(neutral_tweets)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud - Sentimen neutral')
plt.show()

"""###Data Preparation

mengubah teks menjadi huruf kecil, Menghapus mention dan URL ,menghapus tanda baca dan angka dan menghapus stop words
"""

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

"""tokenisasi dan stemming"""

from nltk.stem import PorterStemmer

ps = PorterStemmer()

# Fungsi untuk tokenisasi dan stemming
def stem_text(text):
    tokens = text.split()
    return ' '.join([ps.stem(word) for word in tokens])

df['stemmed_text'] = df['clean_text'].apply(stem_text)

"""TF ID vectorizer"""

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(df['stemmed_text'])
y = df['Label']  # Label target

"""membagi data train dan test"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""## Modelling

model devault linear svc
"""

from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

# Membuat model SVM dasar
linear_svc_model = LinearSVC()  # Menggunakan parameter default
linear_svc_model.fit(X_train, y_train)

# Evaluasi model pada data uji
y_pred = linear_svc_model.predict(X_test)
print(classification_report(y_test, y_pred))

"""tuning parameter model linear svc menggunakan grid search"""

from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV

# Definisikan parameter untuk GridSearch
param_grid = {
    'C': [0.1, 1, 10, 100],
    'penalty': ['l2'],  # LinearSVC hanya mendukung 'l2' jika dual=True
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