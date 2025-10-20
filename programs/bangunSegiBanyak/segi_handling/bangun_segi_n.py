import math
import SegiBanyakUtils as utl

class Segi_n:
	def __init__(self):
		self.get_attr()
		
	@property
	def segi(self):
		return self._segi
		
	@segi.setter
	def segi(self, segi):
		self._segi = self.fixed_value(segi)
		
	@property
	def circumradius(self):
		return self._circumradius
	
	@circumradius.setter
	def circumradius(self, cradius):
		self._circumradius = cradius
	
	@property
	def variants(self):
		return self._variants
	
	@variants.setter
	def variants(self, variants):
		self._variants = variants

	def fixed_value(self, value):
		if value < 0:
			value = abs(value)
		if value < 3:
			value = 3
		return value
			
	def nama_segi_n(self):
		nama = ''
		match self._segi:
			case 3:
				nama = 'trigon'
			case 4:
				nama = 'tetragon'
			case 5:
				nama = 'pentagon'
			case 6:
				nama = 'heksagon'
			case 7:
				nama = 'heptagon'
			case 8:
				nama = 'oktagon'
			case 9:
				nama = 'nanogon'
			case 10:
				nama = 'decagon'
			case 11:
				nama = 'undecagon'
			case 12:
				nama = 'dodecagon'
			case 13:
				nama = 'tridecagon'
			case 14:
				nama = 'tetradecagon'
			case _:
				nama = f'Polygon {self._segi}'
		
		return nama
	
	def sudut_interior(self):
		y = 360 / self._segi
		return y
	
	def sudut_eksterior(self):
		x = 180 - self.sudut_interior()
		return x
	
	def hitung_inerradius(self):
		r = self._circumradius * math.cos(math.pi/ self._segi)
		return r
	
	def hitung_pjg_sisi(self):
		a = self._circumradius * (math.sqrt(2 - (2 * math.cos(math.radians(360)/self._segi))))
		return a
		
	def hitung_luas(self):
		luas = (self._segi/2) * (self._circumradius**2) * (math.sin(math.radians(360)/self._segi))
		return luas
		
	def hitung_keliling(self):
		keliling = self._segi * self.hitung_pjg_sisi()
		return keliling
		
		
	def get_attr(self):
		segi = utl.get_num('Masukkan Jumlah Segi? ')
		circumradius = utl.get_num('Masukkan nilai circum radius? ', start = 0, data_type = float)
		
		self.segi = segi
		self.circumradius = circumradius
		
	def __eq__(self, other):
		return self.__class__.__name__ == other.__class__.__name__
	
		
	def __str__(self):
		return f'''Segi-{self._segi} atau {self.nama_segi_n()}, Circum Radius: {self.circumradius} cm
Sudut Interior = {self.sudut_interior()}
Sudut Eksterior = {self.sudut_eksterior()}
Apothem atau Inner Radius = {self.hitung_inerradius()}
Panjang Sisi = {self.hitung_pjg_sisi()} cm
Keliling = {self.hitung_keliling()} cm
Luas = {self.hitung_luas()} cm²'''
		
