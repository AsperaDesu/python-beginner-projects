import math


def main():
	print('Menampilkan Bilangan Prima')
	
	awal = int(input('Awal: '))
	akhir = int(input('Akhir: '))

	prima(awal, akhir)
	
	
def sof(n):
	prima = [True for _ in range(n + 1)]
	prima [0] = prima [1] = False
	
	for i in range(2, int(math.sqrt(n)) + 1):
		prima[i] = False
		for j in range(i*i , n + 1, i):
			prima[j] = False
		
	return [i for i in range(2, n + 1) if prima[i]]
	
	
def prima(x, y):
	kumpulan = sof(y)
	
	kumpulan = [i for i in kumpulan if i >= x]
		
	for hitung, i in enumerate(kumpulan, 1):
		print(i, end = '   ' )
		
		if hitung % 10 == 0:
			print()
			 
		
		
if __name__ == '__main__':
	main()
