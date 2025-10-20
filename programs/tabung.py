import math
r = int(input("Jari-Jari (cm)? "))
t = int(input("Tinggi (cm)? "))
v = math.pi * r**2 * t
lPerm = 2 * math.pi * r * (r+t)
lTanpa =  math.pi * r * (r+2*t)

print("TABUNG")
print("---------")
print("Nilai PI =",math.pi)
print("Radius = {0:d} cm".format(r))
print("Tinggi = {0:d} cm".format(t))
print("Volume = {0:.3f} cm kubik".format(v))
print("Luas Permukaan dengan Tutup = {0:.3f} cm persegi".format(lPerm))
print("Luas Permukaan tanpa Tutup = {0:.3f} cm persegi".format(lTanpa))

