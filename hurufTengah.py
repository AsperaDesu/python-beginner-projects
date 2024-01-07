nama = input("Nama : ")
panjang = len(nama) 
spasi = ","
tengah = panjang // 2

if panjang % 2 == 0:
	tengah2 = tengah - 1
	print(nama[tengah2] + nama[tengah])
else:
	print(nama[tengah])
