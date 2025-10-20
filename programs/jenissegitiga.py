print("Menentukan Jenis Segitiga")
print("-------------------------------")
a = input("Panjang sisi penyiku pertama a? ")
b = input("Panjang sisi penyiku kedua b? ")
c = input("Panjang sisi miring c? ")

a = int(a)**2
b = int(b)**2
c = int(c)**2

if c == b + a:
	ket = "Segitiga Siku-Siku"
			
if c > b + a:
	ket = "Segitiga Tumpul"

if c < b + a:
	ket = "Segitiga Lancip"

print()

print(ket)

