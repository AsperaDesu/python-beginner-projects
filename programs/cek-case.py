print("Menentukan Jenis Huruf")
print("-"*25)

kalimat = input("Isikan sebuah kalimat? ")

if kalimat == kalimat.upper():
    ket = "HURUF KAPITAL SEMUA"
else:
    if kalimat == kalimat.lower():
        ket = "huruf kecil semua"
    else:
        if kalimat == kalimat.title():
            ket = "Huruf Pertama Setiap Kata Dalam Huruf Kapital"
        else:
            if kalimat == kalimat.capitalize():
                ket = "Huruf pertama kalimat huruf kapital"
            else:
                ket = "KoMBInASI hURUf KAPtiTaL dan hURuF kECiL YaNG TidAK jElaS"

print(f"'{kalimat}' ditulis dalam '{ket}'")