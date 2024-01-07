print("Menentukan Kelompok Karakter")
print("-" * 30)
teks = input("Isikan Sebuah Teks? ")

print()

if teks.isalpha:
	ket = "Huruf Semua"
	if teks.isalnum() and not teks.isdigit() and not teks.isalpha():
			ket = "Campuran Huruf Dan Angka"
	else:		
		if teks.isnumeric():
			ket = "Angka Semua"
		else:
			if not teks.isalpha() and not teks.isnumeric():
				ket = "Campuran dengan Tanda dan Spasi"
			
print(f"{teks} merupakan {ket}")
		
	
