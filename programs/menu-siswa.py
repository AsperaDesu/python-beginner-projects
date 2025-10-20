nama_siswa = ('Dede Kurniawan', 'Sunawati', 'Rosalinda', 'Erwan', 'Hendri', 'Wyndy', 'Alexander Jacob', 'Giovani')

program = ('Coding', 'English','Matematika', 'Coding', 'Matematika', 'Matematika', 'English', 'Coding')

pr = (90, 95, 80, 90, 70, 90, 80, 90)

tugas = (80, 75, 90, 60, 85, 75, 90, 100)

ujian = (60, 80, 100, 90, 100, 80, 75, 85)

zipped = zip(nama_siswa, program, pr, tugas, ujian)
sort_zip = list(zipped)
sort_zip.sort()
zipped = tuple(sort_zip)

isi = ''

while True:
	
	print('-' * 25)
	print('M E N U  S I S W A'.center(25))
	print('-' * 25)

	print('''1. Tabel Nilai Siswa
2. Jumlah Siswa Program
3. Simpulan Nilai Siswa
4. Simpulan Nilai Akhir
5. Keluar''')

	isi = input('\nPilihan anda? ')
	
	if isi == '1':
		print('-' * 66)
		print('No.   Nama Siswa	     Program	    PR     Tugas     Ujian')
		print('-' * 66)

		nomor = 0
		for baris in zipped:
			nomor += 1
			print(f'{nomor:3}   {baris[0]:20}   {baris[1]:10}     {str(baris[2]):3}      {str(baris[3]):3}      {str(baris[4]):3}')

		print('-' * 66)
		print(f'    Nilai Ujian Tertinggi = {max(ujian)}	     Nilai Ujian  Terendah = {min(ujian)}')	
		print('-' * 66)
	
	elif isi == '2':
		print('-' * 27)
		print('Program Siswa'.center(27))
		print('-' * 27)
		print(f'''{'Siswa Coding':17}= {program.count('Coding')} orang
{'Siswa English':17}= {program.count('English')} orang
{'Siswa Matematika':17}= {program.count('Matematika')} orang''')
	
	elif isi == '3':
		print()
		print('-' * 15)
		print('Nilai PR'.center(15))
		print('-' * 15)
		
		lewat = []
		sortPr = list(pr)
		sortPr.sort(reverse = True)
		for nilai in sortPr:
			if nilai not in lewat:
				lewat.append(nilai)
				print(f'{nilai} = {pr.count(nilai)} orang'.center(15))
		
		print()
		
		print('-' * 15)
		print('Nilai TUGAS'.center(15))
		print('-' * 15)
		
		lewat = []
		sortTugas = list(tugas)
		sortTugas.sort(reverse = True)
		for nilai in sortTugas:
			if nilai not in lewat:
				lewat.append(nilai)
				print(f'{nilai} = {tugas.count(nilai)} orang'.center(15))
		
		print()
		
		print('-' * 15)
		print('Nilai UJIAN'.center(15))
		print('-' * 15)
		
		lewat = []
		sortUjian = list(ujian)
		sortUjian.sort(reverse = True)
		for nilai in sortUjian:
			if nilai not in lewat:
				lewat.append(nilai)
				print(f'{nilai} = {ujian.count(nilai)} orang'.center(15))
	
	elif isi == '4':
		print('-' * 66)
		print('No.   Nama Siswa	    Program      Total   Rata-Rata   Huruf')
		print('-' * 66)
		
		nomor = 0
		for baris in zipped:
			nomor += 1
			total = baris[2] + baris[3] + baris[4]
			rata = total / 3
			print(f'{nomor:3}   {baris[0]:20}  {baris[1]:10}    {str(total):3}      %4.2f       ' % (rata), end = '')
			
			if rata > 85:
				print('A')
			elif rata > 75:
				print('B')
			elif rata > 60:
				print('C')
			
		print('-' * 66, end = '')
	
	elif isi == '5':
		break
		
	input('\n\nTekan ENTER untuk melanjutkan!')
	print()
			
			
