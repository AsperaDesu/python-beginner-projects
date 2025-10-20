k = input("Isikan Sebuah Kata? ")
l = int(input("Lebar Yang Diinginkan? "))

kata = k[0].upper() + k[1:-1] + k[-1].upper()

kiri = kata.ljust(l)
kanan = kata.rjust(l)
tengah = kata.center(l)
s = "="

print("Teks Rata Kiri %3s" % (s), "|" + kiri + "|")
print("Teks Rata Kanan %2s" % (s), "|" + kanan + "|")
print("Teks Rata Tengah %1s" % (s), "|" + tengah + "|")
