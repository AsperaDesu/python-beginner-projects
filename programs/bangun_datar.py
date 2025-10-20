import math

OPTIONS  = ['1. Persegi Panjang', '2. Belah Ketupat', '3. Lingkaran', '0. Keluar']
DISPLAY_OPT = '\n'.join(OPTIONS)
MENU = f'''BANGUN DATAR
-------------
{DISPLAY_OPT}'''


class PersegiPanjang:
	def __init__(self, panjang, lebar):
		self.panjang = panjang if panjang else float(18)
		self.lebar = lebar if lebar else float(9)
	
	def hitung_luas(self):
		return self.panjang * self.lebar
		
	def hitung_keliling(self):
		return 2 * (self.panjang + self.lebar)
	
	
	def __str__(self):
		return f'''Persegi Panjang:
	Panjang	: {self.panjang} cm
	Lebar	: {self.lebar} cm'''
	

class BelahKetupat:
	def __init__(self, diagonal1 = 28, diagonal2 = 15):
		self.diagonal1 = diagonal1 if diagonal1 else float(28)
		self.diagonal2 = diagonal2 if diagonal2 else float(15)
		
	def hitung_luas(self):
		return (self.diagonal1 * self.diagonal2) / 2
	
	def hitung_keliling(self):
		return 4 * math.sqrt((self.diagonal1 / 2)**2 + (self.diagonal2 / 2)**2)
	
	
	def __str__(self):
		return f'''Belah Ketupat:
	Diagonal 1: {self.diagonal1} cm
	Diagonal 2: {self.diagonal2} cm'''
	

class Lingkaran:
	def __init__(self, radius = 7):
		self.radius = radius if radius else float(7)
	
	def hitung_luas(self):
		return math.pi * self.radius**2
		
	def hitung_keliling(self):
		return 2 * math.pi * self.radius
		
		
	def __str__(self):
		return f'''Lingkaran:
	Jari-jari (Radius): {self.radius} cm
	Diameter : {self.radius * 2} cm'''
	
	
	
def main():
	pilihan = '3'
	while pilihan != '0':
		print(MENU)
		pilihan = input('Pilihan Anda? ').strip()
		
		if not pilihan.isdigit():
			print()
			continue
		
		print()
		match pilihan:
			case '1':
				print('Membuat Bangun Persegi Panjang >>>')
				panjang = get_int('Panjang? ')
				lebar = get_int('Lebar? ')	
				obj = PersegiPanjang(panjang = panjang, lebar = lebar)
				
			case '2':
				print('Membuat Bangun Belah Ketupat >>>')
				d1 = get_int('Diagonal 1? ')
				d2 = get_int('Diagonal 2? ')
				obj = BelahKetupat(d1, d2)
			
			case '3':
				print('Membuat Bangun Lingkaran >>>')
				radius = get_int('Jari-jari (Radius)? ')
				obj = Lingkaran(radius)
			
			case '0':
				continue
			
			case _:
				print('Isikan pilihan yang tersedia\n')
				continue
		
		print()
		print(obj)
		print(f'''	Luas = {obj.hitung_luas()} cm² 
	Keliing = {obj.hitung_keliling()} cm''')
			
		print()


def get_int(prompt):
	while True:
		try:
			x = input(prompt).strip()
			if x == '':
				return None
			
			x = float(x)
			return x
			
		except ValueError:
			continue
			
			
if __name__ == '__main__':
	main()
	
