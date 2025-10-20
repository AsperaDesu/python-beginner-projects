nama = input("Isikan Sebuah Nama? ")

i = len(nama)
print()
print("=" * len(nama))

while i > 0:
	print(nama[:i ])
	i -= 1  

print("=" * len(nama))

