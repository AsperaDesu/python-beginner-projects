print("Program Nementukan Apakah Nama Yang Diisikan Dalam Huruf Kapital")
print()

nama = input("Isikan Sebuah Nama? ")
keterangan = "BUKAN KAPITAL"

if nama == nama.upper():
	keterangan = "KAPITAL"	

print("Nama Yang Diisikan Dalam Huruf", keterangan, "semuanya.")
