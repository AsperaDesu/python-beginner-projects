ulang = int(input("Jumlah Perulangan? "))
print()

x = 1
for i in range(1, ulang + 1):
	for j in range(1, i + 1):
		print("%2s" % (x), end = "  ")
		x += 1
	print()
