import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca file CSV yang berisi data cuaca
df = pd.read_csv('data_cuaca.csv')

# Menghitung frekuensi untuk setiap suhu
temperature_counts = df['temperature'].value_counts().reset_index()
temperature_counts.columns = ['temperature', 'frequency']

# Set style untuk seaborn agar grafik lebih estetis
sns.set(style="whitegrid")

# 1. Bar Plot Frekuensi Setiap Suhu
plt.figure(figsize=(10, 8))  # Mengatur ukuran grafik
# Membuat bar plot dengan suhu pada sumbu y dan frekuensi pada sumbu x
sns.barplot(x='frequency', y='temperature', data=temperature_counts, palette='Set1', edgecolor='black')
plt.title("Frekuensi Setiap Suhu")  # Judul grafik
plt.xlabel("Frekuensi")  # Label sumbu x
plt.ylabel("Suhu (°C)")  # Label sumbu y
plt.show()  # Menampilkan grafik

# 2. Bar Plot Pola Cuaca Per Kota
plt.figure(figsize=(10, 8))  # Mengatur ukuran grafik
# Membuat bar plot untuk pola cuaca (weather), dipisahkan per kota (hue='city')
sns.countplot(x='weather', hue='city', data=df, palette='viridis')
plt.title("Pola Cuaca Per Kota")  # Judul grafik
plt.xlabel("Pola Cuaca")  # Label sumbu x
plt.ylabel("Frekuensi")  # Label sumbu y
plt.xticks(rotation=45, ha='right')  # Memutar label x-axis agar lebih mudah dibaca
plt.legend(title='Kota')  # Menampilkan legenda untuk kota
plt.show()  # Menampilkan grafik

# 3. Box Plot Suhu Per Kota
plt.figure(figsize=(10, 8))  # Mengatur ukuran grafik
# Membuat box plot untuk suhu, dikelompokkan per kota (x='city', y='temperature')
sns.boxplot(x='city', y='temperature', data=df, palette='Set2')
plt.title("Box Plot Suhu Per Kota")  # Judul grafik
plt.xlabel("Kota")  # Label sumbu x
plt.ylabel("Suhu (°C)")  # Label sumbu y
plt.show()  # Menampilkan grafik
