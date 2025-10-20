nama = input("Isikan Sebuah Nama? ")

print("=" * len(nama))

i = len(nama) 
while i > 0:
	print(nama[i - 1].rjust(i))
	i -= 1 
	 
print("=" * len(nama))

