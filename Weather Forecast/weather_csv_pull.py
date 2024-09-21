import requests
import csv
from collections import Counter

# API Key OpenWeather
api_key = '2d5a949fb8c02ce5edd5557a57f7f8bc'

# Nama kota dan URL API
city = 'Belik'          # Menentukan kota yang dipilih
lang = 'id'             # Menentukan bahasa yang digunakan
complete_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&lang={lang}&units=metric"  # URL yang lengkap

# Mengambil data dari API
response = requests.get(complete_url)
data = response.json()

# Mengecek apakah permintaan berhasil
if response.status_code == 200:
    temperatures = []
    weather_descriptions = []

    # Loop melalui setiap entri cuaca (setiap 3 jam selama 5 hari)
    for forecast in data['list']:
        temp = forecast['main']['temp']
        weather = forecast['weather'][0]['description']
        
        temperatures.append(temp)
        weather_descriptions.append(weather)

    # Menghitung suhu rata-rata, tertinggi, dan terendah
    avg_temp = sum(temperatures) // len(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)

    # Menghitung pola cuaca yang paling sering muncul
    most_common_weather = Counter(weather_descriptions).most_common(1)[0][0]

    # Menyiapkan data untuk disimpan ke CSV
    weather_data = {
        'Kota': city,
        'Suhu rata-rata (C)': avg_temp,
        'Suhu tertinggi (C)': max_temp,
        'Suhu terendah (C)': min_temp,
        'Cuaca yang paling sering': most_common_weather
    }

    # Membuat dan menulis ke file CSV
    csv_file = f'weather_data_{city}.csv'
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=weather_data.keys())
        writer.writeheader()
        writer.writerow(weather_data)

    print(f"Data cuaca berhasil disimpan ke {csv_file}")
else:
    print("Terjadi kesalahan dalam mengambil data dari API")
