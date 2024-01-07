judul = "Program Menambahkan Nol Di Depan"
pembatas = "-"*len(judul)

print(judul)
print(pembatas)
print()

nilai = input("Isikan Nilai? ")
nol = int(input("Jumlah Nol Yang Diinginkan? "))
nilai2 = len(nilai) + nol
ganti = nilai.zfill(nilai2)

print()

print("Perubahan Terjadi:")
print("Nilai: " +  ganti)

