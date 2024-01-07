print("Memeriksa Nama Negara Anggota ASEAN")
print("-" * 40)

negara = input("Isikan Nama Negara? ")
negara2 = negara.lower()
memprakarsai = True
anggotaAsean = True

if negara2 != "indonesia" and negara2 != "malaysia" and negara2 != "singapura" and negara2 != "thailand" and negara2 != "myanmar" and negara2 != "filipina" and negara2 != "vietnam" and negara2 != "laos" and negara2 != "kamboja" and negara2 != "brunei darussalam":
	teks = "bukan negara anggota"
	memprakarsai = False
	anggotaAsean = False			
else:
	teks = "negara anggota"
	if negara2 == "indonesia":
		tokoh = "Adam Malik"
	elif negara2 == "malaysia":
		tokoh = "Tun Abdul Razak"
	elif negara2 == "singapura":
		tokoh = "S. Rajaratnam"
	elif negara2 == "thailand":
		tokoh = "Thanat Khoman"
	elif negara2 == "filipina":
		tokoh = "Narciso Ramos"
	else:
		memprakarsai = False
		
print(f"'{negara.upper()}' adalah {teks} ASEAN")

panah = "--->"

if anggotaAsean and memprakarsai:
	pertama = f"{panah} Negara yang memprakarsai berdirinya ASEAN"
	kedua = f"{panah} Tokoh yang menghadiri {tokoh}"
elif anggotaAsean and not memprakarsai:
	pertama = f"{panah} Bukan negara yang memprakarsai berdirinya ASEAN"
	kedua = ""
else:
	pertama = kedua = ""

print(pertama + "\n" + kedua)
