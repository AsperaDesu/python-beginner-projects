import math

print("MEMBULATKAN KE ATAS ATAU KE BAWAH NILAI PECAHAN")
print()

nilai_pecahan = float(input("Isikan Sebuah Nilai Pecahan? "))


pilihan = input("Bulatkan Ke [1] Bawah atau [2] Atas? ")

if pilihan == "1":
	rumus = math.floor(nilai_pecahan)
	ket = "BAWAH"
else:
	rumus = math.ceil(nilai_pecahan)
	ket = "ATAS"

print(f"{nilai_pecahan} jika dilakukan pembulatan ke {ket} adalah {rumus}")
