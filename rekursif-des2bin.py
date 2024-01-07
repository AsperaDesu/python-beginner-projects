hasil = ''

def main():
	print('-' * 40)
	print('PROSES KONVERSI DESIMAL KE BINER REKURSIF')
	print('-' * 40)
	
	desimal = int(input("Nilai Desimal Dikonversi? "))
	
	print('\nProses Konversi:')
	txt = konversi(desimal)
	print(txt)
	print(f'--> Desimal 12 = Biner {hasil[::-1]}')
	
def konversi(n, biner = ''):
	if n == 0:
		return ''
		
	biner = str(n % 2)
	n_awal = str(n)
	n = n // 2
	
	globals()['hasil'] += biner
	
	return (f'	{n_awal:>5s} / 2 => Hasil = {n:>4d}, Sisa = {biner}\n') + konversi(n, biner)


if __name__ == '__main__':
	main()
