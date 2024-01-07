import math

print("Menentukan Akar-akar Persamaan Kuadrat")
print("----------------------------------------")

print("ax^2 + bx + c")
print()

a = float(input("Nilai a? "))
b = float(input("Nilai b? "))
c = float(input("Nilai c? "))

diskriminan = b**2 - 4 * a * c

print(f"""
----------------------
|  Diskriminan = {diskriminan} |
----------------------
""")

if diskriminan >= 0:
	x1 =  (-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a
	x2 =  (-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a

teks = ""

if diskriminan == 0:
	ket = "Nyata Dan Sama"
	teks = f"x1 = x2 = {x1}"
else:
	if diskriminan > 0:
		ket = "Nyata Dan Tidak Sama"
		teks = f"x1 = {x1}\nx2 = {x2}"
	else:
		ket = "Imajiner"

print(f"Kedua Akar-Akarnya {ket}")
print(teks)
