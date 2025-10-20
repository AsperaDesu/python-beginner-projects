print("-----------------------")
print("Mencari Nilai Rata-Rata")
print("-----------------------")

print("Isikan -1 kalau sudah selesai!")
print()

nilai = 1
jumlah = -1
total = 1
daftar = ""
while nilai != -1:
	jumlah += 1
	nilai = int(input(f"Nilai ke {jumlah + 1}? "))
	total = total + nilai
	daftar = daftar + str(nilai) + ", "
rata = total / jumlah
daftar = daftar.replace("-1, ", "")
tertinggi = max(daftar.split(", "))

print(f"""
Jumlah Data = {jumlah}
Jumlah Nilai = {total}
Rata-Rata = {rata}
Daftar Nilai  = {daftar[:-2]}
Nilai Tertinggi = {tertinggi}""")
