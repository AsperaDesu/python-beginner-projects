kapasitas = int(input("Kapasitas Minyak (Liter)? "))
ukuran = int(input("Ukuran Botol (Liter)? "))

jb = round(kapasitas / ukuran + 0.5)

print("Jumlah Botol Yang Digunakan Adalah", jb)
