judul = "Program Penyandian Sederhana"
pembatas = "-"*len(judul)

print(judul+"\n"+pembatas)

teks = input("Isikan Sebuah Kalimat? ")

kata1 = 'abcdefghijklmnopqrstuvwxyz'
kata2 = 'defghijklmnopqrstuvwxyzabc'

kata1 = kata1 + kata1.upper()
kata2 = kata2 + kata2.upper()

tabel = teks.maketrans(kata1, kata2)

print("Kalimat Hasil Penyandian: {0:s}".format(teks.translate(tabel)))

