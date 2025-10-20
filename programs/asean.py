print("Memeriksa Nama Negara Anggota ASEAN")
print("-" * 40)

negara = input("Isikan Nama Negara? ")
negara2 = negara.lower()

if negara2 != "indonesia" and negara2 != "malaysia" and negara2 != "singapura" and negara2 != "thailand" and negara2 != "myanmar" and negara2 != "filipina" and negara2 != "vietnam" and negara2 != "laos" and negara2 != "kamboja":
	teks = "bukan negara anggota"
else:
	teks = "negara anggota"

print(f"'{negara.upper()}' adalah {teks} ASEAN")

