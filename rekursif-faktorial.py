import math 


def main():
	print('-' * 30)
	print('MENAMPILKAN PERKALIAN FAKTORIAL')
	print('-' * 30)
	
	faktor = int(input('Faktorial dari? '))
	
	print(f'{faktor}! = {faktorial(faktor)} => {math.factorial(faktor)}')

	
def faktorial(n):
	if n == 1:
		return 1

	return str(n) + '\u00d7' + str( faktorial(n-1))


if __name__ == '__main__':
	main()
