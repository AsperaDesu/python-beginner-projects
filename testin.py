a = [
	[2, 4],
	[6, 8],
	[10, 1]
]

b = [
	[1, 3, 5],
	[7, 9, 2],
]

barisA = 3
kolomA = 2
kolomB = 3

print('Matriks A:')
for el in a:
	print(el)

print('\nMatriks B:')
for el in b:
	print(el)

c = [0] * barisA
for i in range(barisA):
	c[i] = [0] * kolomB

print()

for i in range(barisA):
	for j in range(kolomB):
		#c[i][j] = 0
		st = ""
		for k in range(kolomA):
			st += str(a[i][k])+'*'+str(b[k][j]) + ' + '
			#if k == kolomA-1:
			#	st += '+'
			
			c[i][j] += a[i][k] * b[k][j]
		
		print(st)
			
print('\nMatriks C:')
for el in c:
	print(el)
