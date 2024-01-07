teks = input("Isikan Sebuah Teks? ")

print("=" * 30)

jumlah = 0
vokal = 0
konsonan = 0
angka = 0
ganjil = 0
genap = 0
spasi = 0
tanda = 0 

for i in teks:
	if i.isalpha():
		jumlah += 1	
		if i.lower() in "aiueo":
			vokal += 1
		else:
			konsonan += 1
	elif i.isnumeric():
		angka += 1
		if int(i) % 2 == 0:
			genap += 1
		else:
			ganjil += 1
	elif i == " ":
		spasi += 1
	else:
		tanda += 1
		
print(f"""Jumlah Huruf = {jumlah}
--->Huruf Vokal = {vokal}
--->Huruf Konsonan = {konsonan}
Jumlah Angka = {angka}
--->Ganjil = {ganjil}
---> Genap = {genap}
Jumlah Spasi = {spasi}
Jumlah Tanda = {tanda}
""")
	
