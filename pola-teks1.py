nama = input("Isikan Sebuah Nama? ")

i = 1
print()
print("=" * len(nama))

while i <= len(nama):
	print(nama[:i])
	i += 1 

print("=" * len(nama))

