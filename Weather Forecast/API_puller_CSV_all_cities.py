import requests
import csv


API_KEY = '2d5a949fb8c02ce5edd5557a57f7f8bc'    # API key dari OpenWeatherMap
cities = ["Palembang", "Belik", "Lampung", "Jakarta", "Yogyakarta"] # Daftar kota yang akan diambil datanya
base_url = "http://api.openweathermap.org/data/2.5/weather" # Base URL untuk API OpenWeatherMap

weather_data = []   # List kosong untuk menyimpan data cuaca yang nanti akan ditambhakan dengan argumen .append

# Looping untuk mengambil data cuaca setiap kota
for city in cities:
    parameter = {
        'q': city,  # Nama kota
        'appid': API_KEY,  # API Key
        'units': 'metric',  # Satuan suhu dalam Celsius
        'lang': 'id'  # Mengatur bahasa ke bahasa Indonesia
    }

    response = requests.get(base_url, params=parameter)

    # Cek apakah request berhasil dari URL (status code 200 berarti berhasil/OK)
    if response.status_code == 200:
        data = response.json()

        # Menambahkan data cuaca tanpa pengecekan 'main'
        weather_data.append({
            'city': city,
            'temperature': data['main']['temp'],  # Suhu kota dalam Celsius
            'weather': data['weather'][0]['description']  # Kondisi cuaca dalam bahasa Indonesia
        })
    elif response.status_code == 404:   # kode 404 berarti 'not found', Pengecekan jika terjadi typo pada nama kota atau APi tidak bisa menemukan kota yang diminta
        print(f"Kota {city} tidak ditemukan.") 
    else:
        print(f"Gagal mengambil data untuk kota {city}. Status code: {response.status_code}")   # Jika kode yang diterima selain 200/404 yang menandakan masalah lain
    
# Cek jika ada data yang berhasil diambil sebelum menyimpannya
if weather_data:
    # Simpan data ke file CSV
    csv_file = 'data_cuaca.csv' # Nama dari file CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["city", "temperature", "weather"])
        writer.writeheader()
        writer.writerows(weather_data)

    print(f"Data cuaca telah disimpan ke {csv_file}")
else:
    print("Tidak ada data cuaca yang berhasil diambil.")
