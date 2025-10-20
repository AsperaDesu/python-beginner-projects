class Triangle():
	def __init__(self, variety, name, base, height):
		self.variety = variety if variety else 'Siku-siku'
		self.name = name.upper()
		self.base = base
		self.height = height
	
	def __str__(self):
		return f'''Jenis Segitiga	: {self.variety}
Nama Segitiga	: {self.name}
Panjang Alas	: {self.base}
Tinggi 		: {self.height}'''


def main():
	jenis = input('Jenis Segitiga (Enter: Siku-siku)? ').strip().title()
	nama = input('Nama Segitiga? ').strip()
	
	try:
		alas = int(input('Panjang Alas? ').strip())
		tinggi = int(input('Tinggi? ').strip())		
	except ValueError:		
		print('invalid input')
		
	segitiga1 = Triangle(jenis, nama, alas, tinggi)
	
	print()
	print(segitiga1)


if __name__ == '__main__':
	main()
	
