print("PROGRAM MENENTUKAN APAKAH DUA BUAH NILAI AKAN DITAMBAHKAN ATAU DIGABUNGKAN")
print()

nilai1 = input("Isikan Nilai 1? ")
nilai2 = input("Isikan Nilai 2? ")

print()

print("1. Menambahkan")
print("2. Menggabungkan")

pilihan = input("Pilihan Anda? ")

teks = int(nilai1) + int(nilai2)
ket = "MENAMBAHKAN"

if pilihan == "2":
	teks = nilai1 + nilai2
	ket = "MENGGABUNGKAN"

print()

print("Hasil Yang Diinginkan adalah", ket, "hasil yang didapatkan =", teks)
