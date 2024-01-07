nama = input("Isikan Sebuah Nama? ")

print("=" * (len(nama) * 2))

i = len(nama)

while i > 0:
	print(nama[len(nama) - i].rjust((len(nama) - i) + 1 ) + " " * (i * 2 - 2) +nama[len(nama) - i])
	i -= 1
	
print("=" * (len(nama) * 2))

