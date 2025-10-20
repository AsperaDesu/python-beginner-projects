print("Nilai Radius Negatif Akan Dianggap Positif")
r = int(input("Jari-Jari (cm)? "))
PHI = 3.14
r = abs(r)
luas = PHI * r **2
keliling = 2 * PHI * r
print("LINGKARAN")
print("-----------")
print("Nilai PHI =", PHI)
print("Radius =", r, "cm")
print("Luas = {0:.1f} cm persegi".format(luas))
print("Keliling = {0:.2f} cm".format(keliling))
