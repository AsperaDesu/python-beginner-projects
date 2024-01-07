import math

print("Menentukan Akar-akar Persamaan Kuadrat")
print("----------------------------------------")

print("ax^2 + bx + c")
print()

a = float(input("Nilai a? "))
b = float(input("Nilai b? "))
c = float(input("Nilai c? "))

d = b**2 - 4 * a * c

print(f"""
-----------------------
|  Diskriminan = {d} |
-----------------------
""")

if d >= 0:
	x1 =  (-b + math.sqrt(d)) / 2 * a
	x2 =  (-b - math.sqrt(d)) / 2 * a
else:
	bper2a = -b / 2 * a
	akarDper2a = math.sqrt(math.fabs(d)) / 2 * a

if d == 0:
	ket = "Nyata Dan Sama"
	teks = f"x1 = x2 = {x1}"
else:
	if d > 0:
		ket = "Nyata Dan Tidak Sama"
		teks = f"x1 = {x1}\nx2 = {x2}"
	else:
		ket = "Imajiner"
		teks = f"x1 = {bper2a} + {akarDper2a}j\nx1 = {bper2a} - {akarDper2a}j"
		
print(f"Kedua Akar-Akarnya {ket}")
print(teks)
