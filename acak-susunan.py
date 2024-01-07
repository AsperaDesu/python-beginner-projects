import random
kata1 = input("Kata yang diisikan? ")
kata = kata1.replace(" ", "")

simpan = ""
ulang = 0

while ulang < len(kata):
	posisi = 0
	
	while posisi >= 0:
		angka = random.randrange(0,len(kata))
		sAngka = str(angka)
		posisi = simpan.find("," + sAngka + ",")
	
	simpan = simpan + "," + sAngka + ","
	print(kata[angka], end = " ")
	ulang += 1
