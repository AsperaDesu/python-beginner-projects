ulang = int(input("Jumlah Perulangan? "))

for i in range(ulang):
	txt = ""
	total = 0
	for j in range(i + 1):
		total =  total + j
		txt = txt + str(j) + " + "
	print(txt[0:-2] + "=", str(total))
	print()
