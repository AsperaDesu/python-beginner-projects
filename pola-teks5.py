nama = input("Isikan Sebuah Nama? ")

print()
print("=" * len(nama))

i = 0
while i < len(nama):
	print(nama[i].center(i + ( i + 1)))
	i += 1

print("=" * len(nama))
