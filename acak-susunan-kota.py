import random

baru = []

txt = 'Banda-Aceh, Medan, Palembang, Padang, Bengkulu, Pekanbaru, Tanjung-Pinang, Jambi, Bandar-Lampung, Pangkal-Pinang, Pontianak, Samarinda, Banjarmasin, Palangkaraya, Tanjung-Selor, Serang, Jakarta, Bandung, Semarang, Yogyakarta, Surabaya, Denpasar, Kupang, Mataram, Gorontalo, Mamuju, Palu, Manado, Kendari, Makasar, Ternate, Ambon, Monokwari, Jayapura'
provinsi = txt.split(', ')

acak = provinsi[random.randrange(1, 35)].lower()

for i in acak:
	baru.append(i)

random.shuffle(baru)

print('Ibukota setelah susunan huruf diacak =', end = " ")

for i in baru:
	print(i, end = '')

