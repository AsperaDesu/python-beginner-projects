nilai = 1
ke = 1
daftar = []
lanjut = True

besar = False
sama = False
kecil = False

while True:
	nilai = input(f'Nilai ke-{ke}, (Enter kalau sudah selesai!)? ')
	
	if nilai != "":
		nilai = int(nilai)
		daftar.append(nilai)
	else:
		break
		
	ke += 1

print()
print('Nilai sebelum diurutkan')
print('-'*30)
for i in daftar:
	print(i, end = " ")
print('\n')
print()

print('Proses mengurutkan...')
print('-' * 30) 
for i in range(0, len(daftar)-1):

	for j in range(0, len(daftar)-i-1):	
		tempDaftar = list(daftar)
		temptext = ""
		daftartext = ""
		
		if daftar[j] > daftar[j+1]:
			temp = daftar[j]
			daftar[j] = daftar[j+1]
			daftar[j+1] = temp
			besar = True
		elif daftar[j] < daftar[j+1]:
			kecil = True
		else:
			sama = True
		
		for i in tempDaftar:
			temptext = temptext + str(i) + " "
		temptext = temptext[:-1]
		for i in daftar:
			daftartext = daftartext  + str(i) + " " 
		
		if besar:
			print(temptext, f'karena {daftar[j + 1]} > {daftar[j]} maka posisi {daftar[j + 1]} dan {daftar[j]} dibalik sehingga menjadi {daftartext}')
			besar = False
		elif kecil:
			print(temptext, f'karena {daftar[j]} < {daftar[j+1]} maka posisi {daftar[j]} dan {daftar[j+1]} tidak dibalik sehingga tetap {daftartext}')
			kecil = False
		elif sama:
			print(temptext, f'karena {daftar[j+1]} = {daftar[j]} maka posisi {daftar[j+1]} dan {daftar[j]} tidak dibalik sehingga tetap {daftartext}')
			sama = False
	
	print()

print('\nKesimpulan setelah nilai diurutkan')
print('-'*30)
print(f'Nilai Terbesar: {max(daftar)}')
print(f'Nilai Terkecil: {min(daftar)}')
