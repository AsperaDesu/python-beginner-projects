print("PROGRAM MENENTUKAN APAKAH ADA WHITESPACE DI KANAN NAMA YANG DIISIKAN")
print()

nama = input("Isikan Sebuah Nama? ")
ket = "ADA WHITESPACE"

if nama == nama.strip():
    ket = "TIDAK ADA WHITESPACE"

print("Nama Yang Diisikan {0:s}".format(ket))
