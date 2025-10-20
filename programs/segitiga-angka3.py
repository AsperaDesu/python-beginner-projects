print("1. Segitiga Siku-siku Kiri")
print("2. Segitiga Same Kaki")
print("3. Segitiga Siku-siku Kanan")

jenis = input("Jenis Segitiga? ")
ulang = int(input("Jumlah Ulang? "))
j = ulang
i = 1
txt = ""

print()

if jenis == "1":
	while ulang  >= i:
		print("* " * j)
		i += 1
		j -= 1
elif jenis == "2":
	while ulang >= i:
		txt = "* " * j
		print(txt.center(ulang * 2))
		i += 1
		j -= 1
elif jenis == "3":
	while ulang >= i:
		txt = "* " * j
		print(txt.rjust(ulang * 2))
		i += 1
		j -= 1
	
