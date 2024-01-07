ulang = int(input("Jumlah Ulang? "))
i  = 1
txt = ""

while ulang >= i:
	txt = (str(i) + " ") * i
	print(txt.center(ulang * 2))
	i += 1 
