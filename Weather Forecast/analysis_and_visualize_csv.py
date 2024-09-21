import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca file CSV yang berisi data cuaca
df = pd.read_csv('data_cuaca.csv')

# Set style untuk seaborn agar grafik lebih estetis
sns.set(style="whitegrid")

# Menghitung Rata-rata Suhu dari Semua Kota
average_temperature = df['temperature'].mean()
print(f"Rata-rata suhu dari semua kota: {average_temperature:.2f} °C")  # Menggunakan format dua angka di belakang koma

# Menentukan Kota dengan Suhu Tertinggi dan Terendah
max_temp_city = df.loc[df['temperature'].idxmax()]  # Kota dengan suhu tertinggi
min_temp_city = df.loc[df['temperature'].idxmin()]  # Kota dengan suhu terendah

print(f"Kota dengan suhu tertinggi: {max_temp_city['city']} dengan suhu {max_temp_city['temperature']} °C")
print(f"Kota dengan suhu terendah: {min_temp_city['city']} dengan suhu {min_temp_city['temperature']} °C")

# Menganalisis Pola Cuaca yang Paling Sering Muncul
weather_counts = df['weather'].value_counts()  # Menghitung frekuensi setiap pola cuaca
most_common_weather = weather_counts.idxmax()  # Menentukan pola cuaca yang paling sering muncul
most_common_count = weather_counts.max()  # Jumlah kemunculan pola cuaca yang paling umum

print(f"Pola cuaca yang paling sering muncul: {most_common_weather} dengan jumlah {most_common_count} kali")

# Visualisasi Data

# Visualisasi Rata-rata Suhu Per Kota
plt.figure(figsize=(10, 6))
sns.barplot(x='city', y='temperature', data=df, estimator='mean', palette='Set2')
plt.title("Rata-rata Suhu Per Kota")
plt.xlabel("Kota")
plt.ylabel("Rata-rata Suhu (°C)")
plt.xticks(rotation=45)
plt.show()

# Visualisasi Suhu Tertinggi dan Terendah Per Kota
plt.figure(figsize=(10, 6))
# Mengambil data suhu tertinggi dan terendah
temperature_summary = df[['city', 'temperature']].copy()
temperature_summary['Temp Status'] = ['Tertinggi' if temp == max(df['temperature']) else 'Terendah' if temp == min(df['temperature']) else 'Lainnya' for temp in temperature_summary['temperature']]
sns.barplot(x='temperature', y='city', hue='Temp Status', data=temperature_summary, palette='Set1')
plt.title("Suhu Tertinggi dan Terendah Per Kota")
plt.xlabel("Suhu (°C)")
plt.ylabel("Kota")
plt.legend(title='Status Suhu')
plt.show()

# Visualisasi Pola Cuaca yang Paling Sering Muncul
plt.figure(figsize=(10, 6))
# Menghitung frekuensi pola cuaca
weather_counts = df['weather'].value_counts().reset_index()
weather_counts.columns = ['weather', 'frequency']
sns.barplot(x='frequency', y='weather', data=weather_counts, palette='Set3')
plt.title("Frekuensi Pola Cuaca")
plt.xlabel("Frekuensi")
plt.ylabel("Pola Cuaca")
plt.show()
