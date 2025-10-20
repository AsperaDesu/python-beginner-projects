import random

baris = int(input('Jumlah Baris Matriks? '))
kolom = int(input('Jumlah Kolom Matriks? '))

matrix1 = []
matrix2 = []

for i in range(baris):
	matrix1.append([])
	matrix2.append([])
	
for i in range(baris):
	for j in range(kolom):
		matrix1[i].append(random.randint(0, 20))
		matrix2[i].append(random.randint(0, 20))

for i in range(baris):	
	print('|', end = '  ')
	
	for j in range(kolom):
		print('%2d' % (matrix1[i][j]), end = '   ')
	
	if i == baris // 2:
		print('|   +   |', end = '  ')
	else:			
		print('|       |', end = '  ')
		
	for l in range(kolom):
		print('%2d' % (matrix2[i][l]), end = '   ')
	
	if i == baris // 2:
		print('|   =   |', end = '  ')
	else:			
		print('|       |', end = '  ')
		
	for m in range(kolom):
		print('%2d' % (matrix1[i][m] + matrix2[i][m]), end = '   ')

	print('|')
	
