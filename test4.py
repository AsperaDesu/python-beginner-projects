nilai = input("Isikan Sebuah Nilai? ")
nilai = float(nilai)
keterangan = "Bilangan Bulat"
nilai2 = nilai + 0.5

if nilai < round(nilai2):
	keterangan = "Bilangan Pecahan"

print(nilai, "Adalah", keterangan)
