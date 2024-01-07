import random

awal = 1
akhir = 100
kali = 1
tebakan = False
angka = random.randrange(1, 101)
simpanAkhir = ""
simpanAwal = ""
maxAwal = awal
maxAkhir = akhir

while maxAwal >= awal and maxAkhir >= akhir:
	tebak = int(input(f"Silahkan Tebak Dari {awal} s/d {akhir}, -1 untuk menyerah? "))
	
	prevAwal = awal
	prevAkhir = akhir
	
	if maxAwal < prevAwal:
		maxAwal = prevAwall	
	if maxAkhir < prevAkhir:
		maxAkhir = prevAkhir	
		
	if tebak == -1:
		break

	elif tebak > angka:
		akhir = tebak - 1
		print("Terlalu Besar!")
		
	elif tebak < angka:
		awal = tebak + 1
		("---> Terlalu Kecil!")
	
	elif tebak == angka:
		tebakan = True
		break		
			
	kali += 1
	
if tebakan:
	print("\nTepat Sekali.")
	print(f"Anda membutuhkan {kali} kali untuk mendapatkan angka yang benar!")
else:
	print("\nSayang sekali.\nAnda memilih menyerah!")
	print(f"Anda sudah coba {kali} kali, tetapi belum berhasil menebak!")
