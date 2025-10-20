print('SEGITIGA PASCAL')
print('-' * 15)
baris = int(input('Jumlah Baris? '))
segitiga = []
temp = []

for i in range(baris):
	temp = []
	for j in range(i + 1):		
		if j == 0 or j == i:
			temp.append(1)
		else:
			temp.append(segitiga[i -1][j] + segitiga[i-1][j-1])
	segitiga.append(temp)

print()

for i in segitiga:
	txt = ''
	for j in i:
		txt += str(j) + ' '
	print(txt.center(baris ** 2))
