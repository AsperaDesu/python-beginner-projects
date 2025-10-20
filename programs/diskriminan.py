print("Menentukan Akar-akar Persamaan Kuadrat")
print("----------------------------------------")

a = int(input("Nilai a? "))
b = int(input("Nilai b? "))
c = int(input("Nilai c? "))

ket = "Nyata Dan Sama, yaitu x1 = x2"

diskriminan = b**2 - 4 * a * c

if diskriminan > 0:
	ket = "Nyata Dan Tidak Sama, yaitu x1 <> x2"

if diskriminan < 0:
	ket = "Imajiner"	

print(f"Kedua Akarnya {ket}")
