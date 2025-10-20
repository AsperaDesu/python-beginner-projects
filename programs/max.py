print("MENDAPATKAN NILAI MAKSIMAL DARI 2 ATAU 3 NILAI")
print()

jmlh = input("Jumlah Nilai? ")

print()

if int(jmlh) > 3: print(f"Jumlah Nilai Maksimum 3, Jumlah Nilai {jmlh} Dianggap 3")

if jmlh == "2":
	nilai_1 = int(input("Nilai Ke-1? "))
	nilai_2 = int(input("Nilai Ke-2? "))
	rumus = max(nilai_1, nilai_2)
	minimum = min(nilai_1, nilai_2)
else:
	nilai_1 = int(input("Nilai Ke-1? "))
	nilai_2 = int(input("Nilai Ke-2? "))
	nilai_3 = int(input("Nilai Ke-3? "))
	rumus = max(nilai_1, nilai_2, nilai_3)
	minimum = min(nilai_1, nilai_2, nilai_3)

print()

print(f"Nilai Maksimum Adalah {rumus}")
print(f"Nilai Minimum Adalah {minimum}")
