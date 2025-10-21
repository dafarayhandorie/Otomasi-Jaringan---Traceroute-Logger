# Otomasi-Jaringan---Traceroute-Logger
Pencatatan hasil traceroute

import subprocess
import csv
from datetime import datetime

def run_traceroute(target):
    print(f"Menjalankan traceroute ke {target}...\n")
    try:
        # Jalankan traceroute tanpa opsi -n (untuk versi inetutils)
        result = subprocess.run(
            ["traceroute", target],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode != 0 or not result.stdout.strip():
            print("❌ Tidak ada hasil traceroute. Coba jalankan perintah traceroute manual di terminal untuk memastikan koneksi.")
            print("Error:", result.stderr)
            return None

        print("\n--- Hasil Traceroute ---\n")
        print(result.stdout)

        # Simpan hasil ke CSV
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"traceroute_{target.replace('.', '-')}_{timestamp}.csv"

        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Hop", "Host / IP", "Waktu (ms)"])
            
            for line in result.stdout.splitlines()[1:]:  # Lewati baris pertama
                parts = line.split()
                if len(parts) >= 2:
                    hop = parts[0]
                    host = parts[1]
                    time = " ".join(parts[2:])
                    writer.writerow([hop, host, time])

        print(f"\nTraceroute selesai ✅\nHasil disimpan di: {filename}")
        return filename

    except subprocess.TimeoutExpired:
        print("❌ Traceroute timeout (tidak ada respons dari jaringan).")
        return None

if __name__ == "__main__":
    run_traceroute("8.8.8.8")
