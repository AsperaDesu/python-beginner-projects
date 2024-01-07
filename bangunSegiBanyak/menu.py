import sys
import os 

segiHandlingPath = os.path.abspath('segi_handling')
sys.path.append(segiHandlingPath)

from bangun_segi_n import Segi_n
import SegiBanyakUtils as utl

sys.path.remove(segiHandlingPath)

class Menu_segi_n:	
	def __init__(self, mymenu = ('Segi N', 'Prisma Segi N', 'Limas Segi N', 'Keluar'), pilihan = None):
		self.mymenu = 	mymenu
		self.pilihan = pilihan
		self.segiBanyakList = [0,0,0,0]

		
	@property 
	def mymenu(self):
		return self._mymenu
	
	@mymenu.setter
	def mymenu(self, mymenu):
		self._mymenu = mymenu
		self._display = '\n'.join(f'{number}. {content}' for number,content in enumerate(self._mymenu, start = 1))
		
	@property
	def pilihan(self):
		return self._pilihan
		
	@pilihan.setter
	def pilihan(self, pilihan):
		self._pilihan = pilihan		
	
	def mainProgram(self):
		self.display_menu()
		self.assign_pilihan()
		
	def panjang(self):
		return len(self._mymenu)
		
	def display_menu(self):
		pilih = self.panjang() + 1
		print('<<< M E N U >>>\n' + self._display + '\n')
		pilih = utl.get_num(f'Pilihan Anda 1-{self.panjang()}? ', start = 1, end = self.panjang(), data_type = str)
		self._pilihan = pilih		
	
	def assign_pilihan(self):
		shape = None
		keluar = self.panjang()
		match self._pilihan:
			case '1':
				print('SEGI-N')
				makingNew, foundClass = self.check_availability(Segi_n)
				if makingNew:
					shape = Segi_n()
			case keluar:
				return
				
		if not makingNew:
			shape = foundClass
		else:	
			found = False		
			for cls in self.segiBanyakList:
				if cls == shape:
					self.segiBanyakList[self.segiBanyakList.index(cls)] = shape
					found = True
					break
			if not found:
				self.segiBanyakList.append(shape)
				
		print()
		self.display_segi(shape)

		
	def check_availability(self, search):
		replacing = True
		found = False
		foundClass = None
		for cls in self.segiBanyakList:
			if isinstance(cls, search):
				foundClass = cls
				found = True
				break
		if found:
			buatBaru = utl.yesOrNo('>>>Buat baru (Y/T)? ')
			if buatBaru == 't':
				replacing = False
		
		return replacing, foundClass
		
	def display_segi(self,shape):
		print(f'''----------------------------
SEGI BANYAK YANG DIBUAT
----------------------------
{shape}''')
		
		
	def __str__(self):
		return self._display
			

def main():	
	menu1 = Menu_segi_n()
	pilih = 0
	while pilih != str(menu1.panjang()):		
		menu1.mainProgram()
		pilih = menu1.pilihan
		print()
		
if __name__ == '__main__':
	main()
		
