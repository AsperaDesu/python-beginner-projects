judul = ("Mengganti Sebuah Kata Dengan Kata Lainnya")
pembatas = "-"*len(judul)

print(judul+"\n"+pembatas)

teks = input("Isikan Sebuah Teks? ")
kata = input("Isikan Kata Yang Ingin Diganti? ")
baru = input("Isikan Kata Baru Yang Diinginkan? ")

teks = teks.lower()
kata = kata.lower()

ganti = teks.replace(kata, baru)

print("Kalimat Lama: '{0:s}'".format(teks))
print("Kalimat Baru: '{0:s}'".format(ganti.capitalize()))
