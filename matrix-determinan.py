import random

kotak = int(input('Jumlah Baris dan Kolom Matriks? '))

matrix = [0] * kotak
x = [0] * kotak
y = [0] * kotak

for i in range(kotak):
	matrix[i] = [0] * kotak 
	x[i] = [0] * kotak
	y[i] = [0] * kotak
	
for i in range(kotak):
	for j in range(kotak):
		matrix[i][j] = random.randint(0,5)

print('Matriks A:')

for i in matrix:
	print('|', end = '  ')
	for j in i:
		print(j, end = '  ')
	print('|')


print('\nRumus :')

print('(', end = '')

for i in range(kotak):
	for j in range(kotak):
		print(f'A[{(i+j)%kotak},{j}]', end = '' )
		x[i][j] += (matrix[(i+j) % kotak][j])
		if j < kotak -1:
			print('x' ,end = '')
	if i < kotak - 1:
		print(' + ', end = '')

print(')-')

print('(', end = '')
for i in range(kotak):
	for j in range(kotak):
		print(f'A[{(i+j) % kotak},{kotak-j-1}]', end ='')
		y[i][j] += (matrix[(i+j) % kotak][kotak-j-1])
		if j < kotak -1:
			print('x' ,end = '')
	if i < kotak - 1:
		print(' + ', end = '')
print(')')

print('\nHitungan :')

print('(', end = '')

pertama = 0
sum1 = 0

for i in range(kotak):
	sum1 = 1
	for j in range(kotak):
		print(f'{x[i][j]}', end = '')
		sum1 = sum1 * x[i][j]
		if j < kotak -1:
			print('x', end = '')
	pertama += sum1
	if i < kotak -1: 
		print(' + ', end = '')
print(')-')


print('(', end = '')

kedua = 0
sum2 = 0

for i in range(kotak):
	sum2 = 1
	for j in range(kotak):
		print(f'{y[i][j]}', end = '')
		sum2 = sum2 * y[i][j]
		if j < kotak -1:
			print('x', end = '')
	kedua += sum2
	if i < kotak -1: 
		print(' + ', end = '')
print(')')

print('\nDeterminan Matriks A:')
print(f'Determinan => {pertama} - {kedua} = {pertama - kedua}')

