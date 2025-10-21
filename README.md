Otomasi Jaringan - Traceroute Logger

Program ini merupakan alat otomasi jaringan berbasis Python yang berfungsi untuk menjalankan perintah traceroute secara otomatis dan mencatat hasilnya ke dalam file CSV.
Dengan skrip ini, kamu dapat memantau rute perjalanan paket data menuju host tertentu (misalnya 8.8.8.8) sekaligus menyimpan hasilnya untuk dokumentasi atau analisis lebih lanjut.

Fitur Utama:
- Menjalankan traceroute otomatis ke target yang ditentukan.
- Menampilkan hasil traceroute langsung di terminal.
- Menyimpan hasil ke file CSV dengan format nama file otomatis berdasarkan target dan waktu eksekusi.
- Menangani error dan timeout dengan pesan yang informatif.
- Log waktu setiap hop untuk menganalisis performa rute jaringan.

Cara Kerja
Program menjalankan perintah:
python3 traceroute_monitor.py

Hasil traceroute dibaca dari output terminal.

Setiap hop (lompatan jaringan) diekstrak dan disimpan ke file CSV dalam format:
Hop, Host / IP, Waktu (ms)

File disimpan dengan nama otomatis

Persyaratan
Pastikan sistem kamu memenuhi syarat berikut:
- Sistem operasi Linux / macOS / WSL (Windows Subsystem for Linux)
- Python 3.8.2 / 3.x sudah terinstal
- Paket traceroute tersedia di sistem (instal dengan: sudo apt install traceroute)

Cara Menjalankan
Jalankan skrip:
python3 traceroute_monitor.py

Output di terminal:

Menjalankan traceroute ke 8.8.8.8...


--- Hasil Traceroute ---

traceroute to 8.8.8.8 (8.8.8.8), 64 hops max
  1   10.0.2.2  0.357ms  0.579ms  0.014ms 
  2   10.0.2.2  0.908ms  0.618ms  0.808ms 


Traceroute selesai ✅
Hasil disimpan di: traceroute_8-8-8-8_2025-10-21_01-46-01.csv
