nomor = 1
lanjut = 'y'
nilai = []

while lanjut == 'y' or lanjut == '' and lanjut != 't':
	
	masuk = int(input(f'Nilai ke-{nomor}? '))
	nilai.append(masuk)
	
	lanjut = input("Input lagi [Y/T], Enter berarti 'Y'? ").lower()
	nomor += 1

print('\nNilai Sebelum Diurutkan')
print('-' * 30)

for angka in nilai:
	print(angka, end = " ")

print('\n\nProses mengurutkan...')
print('-' * 30)


for i in range(0, len(nilai) - 1):
	for j in range(i, len(nilai)):
		if nilai [i] > nilai [j]:
			temp = nilai [i]
			nilai [i] = nilai [j]
			nilai [j] = temp
	for angka in nilai:
		print(angka, end = " ")
	print('\n')

print('\nNilai Setelah Diurutkan')
print('-' * 30)
for angka in nilai:
	print(angka, end = ' ')
