nama = input("Isikan Sebuah Nama? ")
nama2 = len(nama) * 2 - 2

print("=" * (nama2 + 1))

i = 0
while i < len(nama):
	print(nama[i], end = " ")
	i += 1
print()

i = 1
while i < len(nama) - 1:
	print(nama[i] + nama[-i - 1].rjust(nama2))
	i += 1

i = 1
while i <= len(nama):
	print(nama[-i], end = " ")
	i += 1

print()

print("=" * (nama2 + 1))

