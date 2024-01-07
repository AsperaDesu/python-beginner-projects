import math

MENU = ['Menaikkan Ukuran', 'Menurunkan Ukuran', 'Kubus A = Kubus B', 'Kubus A > Kubus B', 'Kubus A < Kubus B', 'Kubus A != Kubus B', 'Kubus <= Kubus B', 'Kubus A >= Kubus B']
DISPLAY = 'M E N U\n   ' + ('\n   ').join([f'{number}. {opt}' for number, opt in enumerate(MENU, start = 1)] + ['0. Keluar'])
sub_menu = []
display_sub = ''

class Kubus:
	def __init__(self, nama : str, rusuk : float):
		self.nama = nama.title()
		self.rusuk = rusuk
		
		
	def get_bidang(self):
		return self.rusuk * math.sqrt(2)
		
	def get_ruang(self):
		return self.rusuk * math.sqrt(3)
		
	def get_luasPermukaan(self):
		return 6 * (self.rusuk ** 2)
		
	def get_volume(self):
		return self.rusuk**3
		
	def __iadd__(self,other):
		self.rusuk += other
		return self
		
	def __eq__(self, other):
		return self.rusuk == other.rusuk
		
	def __gt__(self, other):
		return self.rusuk > other.rusuk
	
	def __lt__(self, other):
		return self.rusuk < other.rusuk
		
	def __ne__(self, other):
		return self.rusuk != other.rusuk
	
	def __ge__(self, other):
		return self.rusuk >= other.rusuk
	
	def __le__(self, other):
		return self.rusuk <= other.rusuk
	
	def __str__(self):
		return f'''{self.nama}:
---> Panjang Rusuk = {self.rusuk} cm
---> Panjang Diagonal Bidang = {self.get_bidang()} cm
---> Panjang Diagonal Ruang = {self.get_ruang()} cm'''


def main():
	list_kubus = get_kubus()
	print()
	for kubus in list_kubus:
		print(kubus, '\n')
	print()
	
	while True:
		print(DISPLAY)
		pilih = str(get_num('Pilihan Anda [0 - 6]? ', store = int))
		if pilih == '0':
			break
		
		print('\n')
		print('''================
S U B  M E N U
================''')

		match pilih:
			case '1':
				list_kubus = ubah_ukuran(list_kubus, operator = '+')
			case '2':
				list_kubus = ubah_ukuran(list_kubus, operator = '-')
			case '3':
				evaluate(list_kubus, operator = '=')
			case '4':
				evaluate(list_kubus, operator = '>')
			case '5':
				evaluate(list_kubus, operator = '<')
			case '6':
				evaluate(list_kubus, operator = '!=')
			case '7':
				evaluate(list_kubus, operator = '<=')
			case '8':
				evaluate(list_kubus, operator = '>=')
			case _:
				print('Isikan pilihan yang tersedia')
				continue
		
		print('=' * 30, '\n')


def evaluate(kubus : list, operator):
	number = 0
	pairs = {}
	for i in range(len(kubus)):
		for j in range(len(kubus)):
			if j != i:
				number += 1
				print(f'{number}. {kubus[i].nama} - {kubus[j].nama}')
				pairs[number] = [kubus[i], kubus[j]]
				
	print('0. Keluar')
	
	pilih = int(get_num(f'Pilihan Anda [0 - {number}]? '))
	if pilih == 0:
		return 
		
	chosen_pairs = pairs[pilih]
	match operator:
		case '=':				
			check = chosen_pairs[0] == chosen_pairs[1]
			opt_text = 'sama dengan'
		case '>':
			check = chosen_pairs[0] > chosen_pairs[1]
			opt_text = 'lebih besar dari'
		case '<':
			check = chosen_pairs[0] < chosen_pairs[1]
			opt_text = 'lebih kecil dari'
		case '!=':
			check = chosen_pairs[0] != chosen_pairs[1]
			opt_text = 'tidak sama dengan'
		case '<=':
			check = chosen_pairs[0] <= chosen_pairs[1]
			opt_text = 'lebih besar atau sama dengan'
		case '>=':
			check = chosen_pairs[0] >= chosen_pairs[1]
			opt_text = 'lebih kecil atau sama dengan'
		
	print('>>>', end = ' ')
	if check:
		print(f'Ukuran {chosen_pairs[0].nama} {opt_text} {chosen_pairs[1].nama}')
	else:
		if operator != ' !=':
			print(f'Ukuran {chosen_pairs[0].nama} tidak {opt_text} {chosen_pairs[1].nama}')
		else:
			opt_text = 'sama dengan'
			print(f'Ukuran {chosen_pairs[0].nama} {opt_text} {chosen_pairs[1].nama}')
	
	
def ubah_ukuran(kubus : list, operator : str):
	display_sub(kubus)
	pilih = int(get_num(f'Pilihan Anda [0-{len(kubus)}]? ', batas = len(kubus)))
	if pilih == 0:
		return kubus
	
	chosen_box = kubus[pilih-1]
	print()
	
	match operator:
		case '+':
			ganti = get_num(f'Ukuran {chosen_box.nama} dinaikkan dari {chosen_box.rusuk} cm ---> ? ')
		case '-':
			ganti = -(get_num(f'Ukuran {chosen_box.nama} diturunkan dari {chosen_box.rusuk} cm ---> ? '))
		
	chosen_box += ganti
	for content in kubus:
		print(content, '\n')
	
	return kubus
		
		
def get_kubus():
	kumpulanKubus = []
	while True:
		nama = input('Nama Kubus? ')
		if nama == '':
			if len(kumpulanKubus) >= 1:
				break
			else:
				continue
		
		rusuk = get_num('Panjang Rusuk? ')
		print('rusuk ' ,rusuk)
		kumpulanKubus.append(Kubus(nama, rusuk))
		print()
	
	return kumpulanKubus
	
	
def get_num(prompt, store = float, batas = None):
	while True:
		try:
			x = store(input(prompt))
			break
		except ValueError:
			continue
		
	if batas is not None:
		if x > batas:
			return get_num(prompt, store, batas)
			
	return x 
	
def display_sub(list_kubus : list):
	sub_menu = [content.nama for content in list_kubus]
	display_sub = '\n'.join([f'{number}. {content}' for number, content in enumerate(sub_menu, start = 1)] + ['0. Keluar'])
	print(display_sub)
			
if __name__ == '__main__':
	main()
