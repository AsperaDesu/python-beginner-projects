kata = input("Isikan Sebuah Teks? ")
cari = input("Isikan Kata Dicari? ")

kata = kata.lower()
cari = cari.lower()

kiri = kata.find(cari)
kanan = kata.rfind(cari)

print("Letak", cari.capitalize(), "Dari KIRI Ada Di", kiri)
print("Letak", cari.capitalize(), "Dari KANAN Ada Di", kanan)
