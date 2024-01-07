import random

baris = int(input('Jumlah Baris Matriks Pertama? '))
kolom = int(input('Jumlah Kolom Matriks Pertama? '))
kolomb = int(input('Jumlah Kolom Matriks Kedua? '))

print()

matrix1 = []
matrix2 = []

c = [0] * baris

for i in range(baris):
	c[i] = [0] * kolomb

for i in range(baris):
	matrix1.append([])
	
for i in range(kolom):
	matrix2.append([])

print('Matrix A:')
for i in range(baris):
	for j in range(kolom):
		matrix1[i].append(random.randint(0,10))

for i in matrix1:
	print(i)

print()

print('Matrix B:')
for i in range(kolom):
	for j in range(kolomb):
		matrix2[i].append(random.randint(0,10))			

for i in matrix2: 
	print(i)

print()

print('Matriks C:')
print('Proses Perhitungan: ')

print()

for i in range(baris):
	for j in range(kolomb):
		c[i][j] = 0
		txt = ''
		for k in range(kolom):
			txt += '%2d x %2d' % (matrix1[i][k], matrix2[k][j])
			c[i][j] += matrix1[i][k] * matrix2[k][j]
			if k != kolom - 1:
				txt += '  +  '
			else:
				txt += '  '
		
		print(txt, end = '       ')
	
	print()
	
print()

print('Hasil Perkalian Matriks:')
for i in c:
	print('|', end = '  ')
	for j in i:
		print('%3d' % (j), end = '  ')
	print('|')

