judul = input("masukkan Judul: ")
judul = judul.title()

judul2 = judul.replace(judul[judul.find(" ") -  1], judul[judul.find(" ") - 1].upper())

print(judul2.replace(judul2[-1], judul2[-1].upper()))
