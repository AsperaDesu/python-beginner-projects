nama_siswa = ('Dede Kurniawan', 'Sunawati', 'Rosalinda', 'Erwan', 'Hendri', 'Wyndy', 'Alexander Jacob', 'Giovani')

program = ('Coding', 'English','Matematika', 'Coding', 'Matematika', 'Matematika', 'English', 'Coding')

pr = (90, 95, 80, 90, 70, 90, 80, 90)

tugas = (80, 75, 90, 60, 85, 75, 90, 100)

ujian = (60, 80, 100, 90, 100, 80, 75, 85)

print('Nama Siswa:')

for i in range(1, 9):
	print('\t', i, nama_siswa[i - 1])


print('\nProgram:')

for i in range(1, 9):
	print('\t', i, program[i - 1])
	
print('\nPR:')

for i in range(1, 9):
	print('\t', i, pr[i - 1])

print('\nTugas:')

for i in range(1, 9):
	print('\t', i, tugas[i - 1])

print('\nUjian:')

for i in range(1, 9):
	print('\t', i, ujian[i - 1])

print('\nZip Siswa:')
zipped = zip(nama_siswa, program, pr, tugas, ujian)

for baris in zipped:
	print('\t' + str(baris)) 
