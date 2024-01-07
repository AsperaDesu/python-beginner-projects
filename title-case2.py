judul = input("Masukkan Sebuah Judul? ")
judul2 = judul.title()
txt = ""

for i in judul2:
	while not i == " ":
		txt = txt + i
	else:
		txt = txt + judul2.find[i - 1].upper()

print(txt)
