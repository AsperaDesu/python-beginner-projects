judul = "Program Penyandian Sederhana"
pembatas = "-"*len(judul)

print(judul+"\n"+pembatas)

teks = input("Isikan Sebuah Kalimat? ")
teks = teks.lower()

tabel = teks.maketrans('abcdefghijklmnopqrstuvwxyz','defghijklmnopqrstuvwxyzabc')

print("Kalimat Hasil Penyandian: {0:s}".format(teks.translate(tabel)))
