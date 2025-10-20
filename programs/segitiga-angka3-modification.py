print("1. Segitiga Siku-siku Kiri")
print("2. Segitiga Same Kaki")
print("3. Segitiga Siku-siku Kanan")

jenis = input("Jenis Segitiga? ")
ulang = int(input("Jumlah Ulang? "))
j = ulang
i = 1
txt = ""
result = ""

print()

if jenis == "1":
	while ulang  >= i:
		txt = txt + "* " * j + "\n"
		i += 1
		j -= 1
	result = txt
elif jenis == "2":
	while ulang >= i:
		txt = txt + "* " * j + "\n"
		result = result + txt.center(ulang *2)
		i += 1
		j -= 1
	
elif jenis == "3":
	while ulang >= i:
		txt = (txt + "* " * j + "\n").rjust(ulang * 2)
		i += 1
		j -= 1
	result = txt
		
print(result)
	
