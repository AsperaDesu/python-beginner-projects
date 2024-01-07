import math

class Segitiga:
	def __init__(self, jenis, nama, alas, tinggi):
		self.jenis = jenis
		self.nama = nama
		self.alas = alas
		
		self.namasisi()
		
		panjangSisi = []
		sisi1 = alas
		
		match jenis:
			case 'Siku-Siku':
				sisi2 = tinggi
				sisi3 = math.sqrt(alas** 2 + tinggi**2)
			
			case 'Sama Sisi':
				sisi2, sisi3 = alas, alas
				tinggi = math.sqrt(alas ** 2 - (alas/2)**2)
				
			case 'Sama Kaki':
				sisi2 = math.sqrt(alas** 2 + tinggi **2)
				sisi3 = sisi2 
			
			case 'Sembarang':
				print()
				sisi2 = float(input(f'Panjang Sisi {self.namaSisi[1]}? '))
				sisi3 = float(input(f'Panjang Sisi {self.namaSisi[2]}? '))
		
		self.panjangSisi = [sisi1, sisi2, sisi3]
		
		if self.jenis == 'Sembarang':			
			if self.ceksisi():				
				s = 0.5 * (sisi1 +  sisi2 + sisi3)
				luas = math.sqrt(s * (s - sisi1) * (s - sisi2) * (s - sisi3))
				tinggi = 2 * luas / self.alas
			else:
				self.tinggi  = 0
				self.alas = 0 
				self.panjangSisi = [0,0,0]
		
		self.tinggi = tinggi
		
	def namasisi(self):
		namaSisi = []
		for i in range(len(self.nama)):
			namaSisi.append(''.join(sorted(self.nama[i]+self.nama[(i+1) % 3])))
		self.namaSisi = namaSisi
	
	
	def ceksisi(self):
		sisi1, sisi2, sisi3 = self.panjangSisi
		if (sisi1 + sisi3) > sisi2 and (sisi3 + sisi2) > sisi1 and (sisi1 + sisi2) > sisi3:
			return True
		else:
			return False
				
	
	def hitung_keliling(self):
		return sum(self.panjangSisi)
	
	
	def hitung_luas(self):
		return 0.5 * self.alas * self.tinggi


	def print_sisi(self):		
		print('Nama-nama Sisi & Panjangnya: ')
		for i in range(3):
			print(f'	Sisi {self.namaSisi[i]}: {self.panjangSisi[i]} cm')
	
	
	def __str__(self):
		return (f'''Jenis Segitiga	: {self.jenis}
Nama Segitiga	: {self.nama}
Panjang Alas	: {self.alas} cm
Tinggi		: {self.tinggi} cm''')
	
	
def main():
	prompt_tinggi = True
	tinggi = 0

	jenis = 'asdf'
	while jenis not in ['Siku-Siku', 'Sama Sisi', 'Sama Kaki', 'Sembarang', '']:
		jenis = input('Jenis Segitiga (Enter: Siku-Siku)? ').title().strip()
	
	jenis = 'Siku-Siku' if jenis == '' else jenis
	if jenis == 'Sama Sisi' or jenis == 'Sembarang':
		prompt_tinggi = False
	
	nama = 'asdf'
	while len(nama) != 3:
		nama = input('Nama Segitiga? ').upper().strip()
	
	alas = float(input('Panjang Alas (cm)? ').strip())
	if prompt_tinggi:
		tinggi = float(input('Tinggi (cm)? ').strip())
		
	segitiga = Segitiga(jenis, nama, alas, tinggi)
	print()
	
	print(f'{segitiga}\n')
	segitiga.print_sisi()
	
	print(f'''\nKeliling Segitiga = {segitiga.hitung_keliling()} cm
Luas Segitiga = {segitiga.hitung_luas()} cm²''')
		
		
if __name__ == '__main__':
	main()
