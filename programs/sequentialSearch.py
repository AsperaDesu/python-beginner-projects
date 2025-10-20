jml = int(input('Jumlah Data? '))
data = []

for nomor in range (1, jml + 1):
	tambah = int(input(f'Nilai ke-{nomor}? '))
	data.append(tambah)

cari = int(input('\nNilai yang dicari? '))

ada = False
sama = []

for i in range(jml):
	if data[i] == cari:
		ada = True
		posisi = i + 1
		sama.append(posisi)

if ada:
	for i in range(len(sama)):
		print(f'Nilai {cari} ditemukan di posisi {sama[i]}!')
	
else:
	print(f'Nilai {cari} tidak ditemukan!!!')
