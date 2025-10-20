import random

baru = []
kotaBaru = ''

print('-' * 34)
print('PERMAINAN MENEBAK IBUKOTA PROPINSI')
print('-' * 34)

txt = 'Banda-Aceh, Medan, Palembang, Padang, Bengkulu, Pekanbaru, Tanjung-Pinang, Jambi, Bandar-Lampung, Pangkal-Pinang, Pontianak, Samarinda, Banjarmasin, Palangkaraya, Tanjung-Selor, Serang, Jakarta, Bandung, Semarang, Yogyakarta, Surabaya, Denpasar, Kupang, Mataram, Gorontalo, Mamuju, Palu, Manado, Kendari, Makasar, Ternate, Ambon, Monokwari, Jayapura'
provinsi = txt.split(', ')

acak = provinsi[random.randrange(1, 34)].lower()

for i in acak:
	baru.append(i)

random.shuffle(baru)

for i in baru:
	kotaBaru = kotaBaru + i
	
print('---------------')
print('|' + kotaBaru.center(13) + '|', '<-- Ibukota apakah ini?')
print('---------------')

lst_asli = []

for i in range(26):
	lst_asli.append(0)
	
reset = list(lst_asli)

for huruf in acak:
	lst_asli[ord(huruf) - 97] += 1

isi = ''
nomor = 0
konfirmasi = 't'
score = 100.00
hint = 0
hintList = []
hintTxt = ''

while konfirmasi != 'y':
	
	print('Score: %.2f Hint: %d' % (score, hint))
	
	nomor += 1
	isi = input(f'	Percobaan ke-{nomor}, silahkan ditebak? ')
	
	if isi == '=':
		konfirmasi = input('Anda memutuskan untuk menyerah (Y/T)? ')
		
		if konfirmasi == 't':
			nomor -= 1
	
	elif isi == 'tolong':
		
		score -= 50/len(acak)
		hintTxt = ''
		
		hint += 1
		for i in range(hint):
			hintTxt = hintTxt + acak[i] + ' '
		
		print('--->', hintTxt , end = '')
		print('_ ' * (len(acak) - hint))
				
	elif isi != acak:
		
		lst_isi = list(reset)
		
		for huruf in isi.replace(' ', ''):
			lst_isi[ord(huruf) - 97] += 1
		
		for i in range(26):
			lst_isi[i] -= lst_asli[i]
		
		print('	', end = '')
		
		for i in range(26):
			if lst_isi[i] == 0:
				continue
			else:
				print(chr(i+97), ':', end = '')
				
				if lst_isi[i] > 0:
					print('+' + str(lst_isi[i]), end = '	    ')
				else:
					print(lst_isi[i], end = '	    ')
		
		print('\n	Salah, silahkan dicoba lagi...')
		score -= 2
	
	else:
		print(f'\n>>>Tepat tebakan anda, anda melakukan {nomor} kali untuk mendapatkan nama ibukota yang benar!')
		break
	
	
	
		
