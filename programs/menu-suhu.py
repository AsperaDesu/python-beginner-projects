mymenu = ('[A] Celcius ke Fahrenheit', '[B] Celcius ke Reamur', '[C] Celcius ke Kelvin', '[D] Fahrenheit ke Celcius' , '[E] Fahrenheit ke Reamur', '[F] Fahrenheit ke Kelvin', '[G] Reamur ke Celcius' , '[H] Reamur ke Fahrenheit', '[I] Reamur ke Kelvin', '[J] Kelvin ke Celcius', '[K] Kelvin ke Fahrenheit', '[L] Kelvin ke Reamur', '[Z] Keluar')


def main():
	
	while True:
		print('<<< Menu Konversi >>>')
		print(*mymenu, sep = '\n' )
		
		pilih = input('Pilihan Anda? ').upper()
		


def cel2fah(x):
	return 9/5 * x + 32
	
def cel2rea(x):
	return 4/5 * x
	
def cel2kel(x):
	return x + 273

	
def rea2cel(x):
	return 5/4 * x
	
def rea2fah(x):
	return 9/4 * x + 32
	
def rea2kel(x):
	return 5/4 * x + 273
	


def fah2cel(x):
	return 5/9 * (x - 32)
	
def fah2rea(x):
	return 9/5 * x + 32
	
def fah2kel(x):
	return 4/5 * (x - 273)
	
	

def kel2cel(x): 
	return x + 273
	
def kel2fah(x):
	return 4/9 * (x - 32) + 273
	
def kel2rea(x):
	return 5/4 * x + 273
	

		
		
	
if __name__ == '__main__':
	main() 
	
