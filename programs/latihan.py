nilai = input("Isikan Sebuah Nilai? ")

nilai = float(nilai)
keterangan = "Bilangan Pecahan"

if nilai == round(nilai):
	keterangan = "Bilangan Bulat"

print(keterangan)
