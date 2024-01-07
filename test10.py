kode = input("Jenis Kelamin : (L)aki - Laki / (P)erempuan? ")
kode = kode.strip().upper()

if kode == "L":
	jk = "Laki - Laki"
	print(f"Anda adalah {jk}")
elif kode == "P":
	jk = "Perempuan"
	print(f"Anda adalah {jk}")
else:
	print("invalid input.")
	
