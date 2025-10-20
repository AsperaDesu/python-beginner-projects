nama_siswa = ('Dede Kurniawan', 'Sunawati', 'Rosalinda', 'Erwan', 'Hendri', 'Wyndy', 'Alexander Jacob', 'Giovani')

program = ('Coding', 'English','Matematika', 'Coding', 'Matematika', 'Matematika', 'English', 'Coding')

pr = (90, 95, 80, 90, 70, 90, 80, 90)

tugas = (80, 75, 90, 60, 85, 75, 90, 100)

ujian = (60, 80, 100, 90, 100, 80, 75, 85)

zipped = zip(nama_siswa, program, pr, tugas, ujian)
sort_zip = list(zipped)
sort_zip.sort()
zipped = tuple(sort_zip)

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
