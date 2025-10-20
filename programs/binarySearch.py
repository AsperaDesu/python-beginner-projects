data = []
ada = False
kecil =  False
besar = False
ketemu = False

jml = int(input('Jumlah data? '))

print()
ke = 1

for i in range(jml):
	tambah = int(input(f'Nilai ke-{ke}? '))
	data.append(tambah)
	
	ke += 1

print('\nProses Mengurutkan...')

data.sort()

print('>>>Selesai!!!\n', end = '       ')

for angka in data:
	print(angka, end = " ")

print('\n')

cari = int(input('Nilai yang dicari? '))

print()

akhir = jml - 1
awal = 0

while akhir >= awal:
	
	tengah = ((akhir+awal) // 2)
	
	print(f'Awal = {awal}, Akhir = {akhir}, Tengah = {tengah} Nilai[Tengah] = {data[tengah]}')
	
	if data[tengah] == cari:
		ada =  True
		posisi = tengah + 1
		break
			
	else:
		if cari > data[tengah]:
			awal = tengah + 1
			kecil = True

		else:
			akhir = tengah - 1
			besar = True

	if kecil:
		print(f'>>> Terlalu kecil, awal dinaikkan menjadi {awal}')
		
	elif besar:
		print(f'>>> Terlalu besar, akhir diturunkan menjadi {akhir}')

	input('Tekan Enter untuk lanjut!')
	print()

print()

if ada:
	print(f'Nilai {cari} ditemukan di posisi {posisi}!')
else:
	print(f'Nilai {cari} tidak ditemukan!')
