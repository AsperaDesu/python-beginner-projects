judul = "Menghitung Munculnya Kata"
pemisah = "-"*len(judul)

print(judul)
print(pemisah)

kata = input("Isikan Sebuah Teks? ")
cari = input("Isikan Kata Yang Ingin Dihitung? ")

lowerkata = kata.lower()
lowercari = cari.lower()

tanpa = kata.count(cari)
ada = lowerkata.count(lowercari)

print("Jumlah Kata '" + cari + "' ada", tanpa, "buah jika membedakan huruf kapital dan huruf kecil")
print("Jumlah Kata '" + cari + "' ada", ada, "buah jika tidak membedakan huruf kapital dan huruf kecil")
