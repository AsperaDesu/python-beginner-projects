r = int(input("Jari-Jari (cm)? "))

PHI = 3.14
import math

luas = math.pi * r **2
keliling = 2 * math.pi * r
print("LINGKARAN")
print("-----------")
print("Nilai PHI =", math.pi)
print("Radius =", r, "cm")
print("Luas = {0:.1f} cm persegi".format(luas))
print("Keliling = {0:.2f} cm".format(keliling))
