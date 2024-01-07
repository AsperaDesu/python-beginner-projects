nilai_asli = 35462.81907
print("Nilai ASLI =", nilai_asli)
print()
print("Pembulatan ke:")
print("1. Bulatan ke 3 angka desimal") #3
print("2. Bulatan ke 2 angka desimal") #2
print("3. Bulatan ke 1 angka desimal") #1
print("4. Bulatan ke satuan") #0
print("5. Bulatan ke puluhan") #-1
print("6. Bulatan ke ratusan") #-2
print("7. Bulatan ke ribuan") #-3
print("8. Bulatan ke puluh ribuan") #-4

no = int(input("Pilih No? "))
angka = 4 - no
bulat = round(nilai_asli, angka)
print("Nilai PEMBULATAN =", bulat)
