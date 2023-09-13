# Konversi Detik ke Dalam Format 00:00:00
detik = int(input("Masukkan jumlah detik = "))

jam = detik // 3600 # 1 jam = 3600 detik

''' 
Sisa dari pembagian jam dikonversi ke menit. Kemudian
dibagi 60 karena 1 menit = 60 detik
'''
menit = (detik % 3600) // 60

'''
Sisa dari pembagian jam dan sisa dari pembagian menit akan akan dikonversi
ke detik
'''
detik = (detik % 3600) % 60

print(f"{jam:02d}:{menit:02d}:{detik:02d}")
