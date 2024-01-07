import math

p = int(input("Panjang? "))
l = int(input("Lebar? "))
i = 0

print()
print()
print("Persegi Panjang:\n")

while i < l:
	if i == math.ceil((l / 2 - 1)):
		print("* " * p, f"{l} cm")
	else:
		print("* " * p)	
	i += 1

tengah = math.ceil(((p * 2) / 2 - 1))

print(f"%{tengah}d cm" % (p))
