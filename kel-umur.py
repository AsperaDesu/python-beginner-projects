print("Menentukan Kelompok Umur")
print("----------------------------")

umur = int(input("Isikan Umur? "))

if umur > 65:
	ket = "MANULA"
else:
	if umur > 35:
		ket = "DEWASA AKHIR"
	else:
		if umur > 25:
			ket = "DEWASA AWAL"
		else:	
			if umur > 16:
				ket = "REMAJA AKHIR"
			else:	
				if umur > 11:
					ket = "REMAJA AWAL"
				else:	
					if umur > 4:
						ket = "KANAK-KANAK"
					else:
						ket = "BALITA"
						
print()

print(f"{umur} tahun dikelompokkan sebagai '{ket}'")
