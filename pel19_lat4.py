menu = set()
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
konsonan = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vokal = ['a', 'e', 'i', 'o', 'u']


dicts = {'Konsonan Kecil': konsonan,
'Konsonan Besar': [i.upper() for i in konsonan],
'Vokal Kecil': vokal,
'Vokal Besar': [i.upper() for i in vokal],
'Angka': [str(i) for i in range(10)],
'Spasi': ' '}


kalimat = input('Kalimat: ')

def main():

	get_menu(kalimat)
	menu2 = sorted(list(menu))
	print(menu2)
	
	teks = text(menu2)
	choice(menu2, teks)
	
	
def get_menu(x):
	for i in x:
		if i.isalpha():
			if i in 'aiueo':
				menu.add('Vokal Kecil')
			elif i in 'AIUEO':
				menu.add('Vokal Besar')
			elif i not in 'aiueo' and i.islower():
				menu.add('Konsonan Kecil')
			else:
				menu.add('Konsonan Besar')
		
		elif i.isdigit():
			menu.add('Angka')
			
		elif i == ' ':
			menu.add('Spasi')
		
		else:
			menu.add('Tanda ' + i)
			dicts['Tanda '  + i] = i
			
			
def text(txt):
	pilih = []
	
	for i in range(len(txt)):			
		pilih.append(f'{alphabets[i].upper()}. {txt[i]}')
		
	return '\n'.join(pilih)


def choice(y, txt):
	
	pilihan = ''
	
	while pilihan != '0' :
		print('\n<<< M E N U >>>')
		print(txt)
		print() 
		
		pilihan = input('Pilihan Anda? ').upper()
		
		try:
			cari1 = ord(pilihan) - 65
			cari = dicts[y[cari1]]
			hitung = 0
			
			for i in kalimat:
				if i in cari:
					hitung += 1
			
			print()
			print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
			print(f'Jumlah {y[cari1]} = {hitung}')
			print()
			
		except IndexError:
			if pilihan == '0':
				break
			
			else:
				print('isikan pilihan yang benar!')
		
		
main()
