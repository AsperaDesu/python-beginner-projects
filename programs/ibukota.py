import os

def menu_update(menu):
	alert = ' (PERLU DIBACA ULANG!!)'
	
	if menu[0].endswith(alert):
		return menu
	
	menu[0] += alert
	menu[1] += alert	
	return menu
	
	
def refresh(alert):
	if alert: 
		alert = False
	return alert 	

def main():
	default_menu = ['1. Baca Semua dari File: "ibukota.txt"', '2. Baca Tertentu dari File: "ibukota.txt"', '3. Tampilkan Hasil Baca','4. Tambahkan di File: "ibukota.txt"', '5. Sisipkan di File: "ibukota.txt"', '6. Hapus di File: "ibukota.txt"', '7. Simpan Sebagai File Baru', '8. Keluar']
	menu = list(default_menu)
	refresh_alert = False
	data = None
	baris = None
	max_negara = 0
	max_ibukota = 0
	while True:
		display_menu(menu)
		print()
		
		masukan = get_choice('Pilih dari [1-8]? ')
		print()
		
		match masukan:
			case '1':
				print('>>>Sedang membaca...')
				baris, refresh_alert, extract = read_file(refresh_alert)
				data = extract[0]
				max_negara, max_ibukota = extract[1]
				
				print('>>> Selesai membaca...\n')
				
				menu = list(default_menu)
				
			case '2':
				print('>>>Sedang membaca...\n')
				baris, refresh_alert, extract = read_spec(refresh_alert)
				data = extract[0]
				max_negara, max_ibukota = extract[1]
				print('>>> Selesai membaca...\n')
				
				menu  = list(default_menu)
		
			case '3':
				display_data(data, max_negara, max_ibukota)
				print()
			
			case '4':	
				max_negara, max_ibukota = write_data(max_negara, max_ibukota)
				
				menu = menu_update(menu)
				refresh_alert = True
			
			case '5':
				refresh_alert = insert_data(data)
				print()
				print('>>>Selesai menyisipi...')
			
				if refresh_alert:
					menu = menu_update(menu)
			
			case '6':
				refresh_alert = delete_data(data)
				print( '>>> Selesai menghapus...')
				print
				
				if refresh_alert:
					menu = menu_update(menu)
			
			case '7':
				print(baris)
				new_save(baris)
				print()
				print('Selesai mengcopy file...')
				
			case '8':
				break
		
		print('=' * 50)
		print()


def display_menu(menu):
	print('<<< M E N U >>>')
	print(*menu, sep = '\n')


def get_choice(prompt : str) -> str:
	masukan = ''
	while not masukan.isdigit(): 
		masukan = input(prompt).strip()
	
	return masukan 
	
	
def read_file(alert : bool) -> list:  #choice 1
	with open('ibukota.txt', 'r') as file:
		baris = file.readlines()
		return baris, refresh(alert), get_data(baris)
	
	
def read_spec(alert : bool) -> list:  # choice 2
	mulai = int(get_choice('Mulai baris? ')) - 1
	sampai = int(get_choice('Sampai baris? ')) - 1
	
	print()
	
	if mulai > sampai:
		print('Invalid Input')
		return read_spec(alert)
	
	with open('ibukota.txt', 'r') as file:
		lines = []
		for line_index, line in enumerate(file, start = 0):
			if mulai <= line_index <= sampai:
				lines.append(line)
			elif line_index > sampai:
				print('EOF reached!!')
				break
		
		return lines, refresh(alert), get_data(lines)
		

def get_data(baris : list) -> list[str]:
	table_data = []
	maks_negara = set()
	maks_ibukota = set()
	
	for row in baris:
		negara, ibukota = row.strip().split(';')
		maks_negara.add(len(negara))
		maks_ibukota.add(len(ibukota))
		table_data.append([negara, ibukota])
	
	maks_negara = max(maks_negara) + 10
	maks_ibukota = max(maks_ibukota) + 5
	
	return table_data, (maks_negara, maks_ibukota)


def display_data(data : list[str, str], maks_negara : int, maks_ibukota : int) -> None:  #choice 3
	if data is not None:
		lines = maks_negara + maks_ibukota + 4
		
		print('-' * lines)
		print('{:<4} {:<{}} {:<{}}'.format('No.', 'Negara', maks_negara, 'Ibukota', maks_ibukota))
		print('=' * lines)
		
		for number, (negara, ibukota) in enumerate(data, start = 1):
			number_str = '%2d  ' % number
			print(f'{number_str} {negara.ljust(maks_negara)} {ibukota.ljust(maks_ibukota)}')
		
		print('-' * lines)
	
	else:
		print('Pilih menu 1 sebelum menampilkan hasil baca!')
	

def write_data(max_negara : int, max_ibukota : int) -> None:  #choice 4
	print('>>> Sedang menambahkan...')
	new_negara = 'p'
	new_ibukota = 'p'
	add = []
	
	while new_negara != '' and new_ibukota != '':
		new_negara = input('Negara? ').strip().title()
		new_ibukota = input('Ibukota? ').strip().title()
		max_negara = max(len(new_negara), max_negara)
		max_ibukota = max(len(new_ibukota), max_ibukota)
		add.append(new_negara + ';' + new_ibukota)
		print()
	
	add.pop()
	
	with open('ibukota.txt', 'a') as file:
		for line in add:
			file.write((line) + '\n')
			
	print()
	print('>>> Selesai menambahkan...')
	
	return max_negara, max_ibukota
	

def insert_data(data : list[str, str]) -> None:  #choice 5
	print('>>>Sedang menyisipi...')
	
	if data is not None:
		negara = input('Negara? ').strip().title()
		ibukota = input('Ibukota? ').strip().title()
		sisip = input('Disisipi setelah negara? ').strip().title()
	
		index = 0
		
		for line in data:
			index += 1
			if line[0] == sisip:
				break
			elif index >= len(data):
				print('Negara tidak ditemukan!! Gagal menyisipkan!')
				return False
		
		data.insert(index, [negara, ibukota])
		
		with open('ibukota.txt', 'w') as file:
			for row in data:
				file.write(f'{row[0]};{row[1]}\n')
		
	else:
		print('Pilih menu 1 sebelum menyisipi negara baru!')
		return False
	
	return True
		

def delete_data(data : list[str, str]) -> None:  # choice 6	
	print('>>> Sedang menghapus...')
	
	if data is not None:
		del_negara = input('Negara? ').strip().title()
		index = -1
		
		for line in data:
			index += 1
			if line[0] == del_negara:
				del data[index]
				break
			elif index >= len(data) - 1:
				print('Negara tidak ditemukan! Gagal menghapus!!')
				return False
		
		with open('ibukota.txt', 'w') as file:
			for row in data:
				file.write(f'{row[0]};{row[1]}\n')
		
		return True
		
	else:
		print('Pilih menu 1 sebelum menghapus negara!')
		return False
	
	return True
		

def new_save(baris : list) -> None:
	if baris is not None:		
		new_file = input('Simpan sebagai file? ').strip()
		
		if os.path.isfile(new_file):
			pilih = input(f'File dengan nama {new_file} sudah ada! Teruskan [Y/T]? ').strip().lower()
			
			match pilih:
				case 'y':
					pass
				case 't':
					print('Gagal mengcopy!!')
					return False
				case _:
					print('Invalid input')
					return new_save(baris)
				
		with open(new_file, 'w') as file:
			for row in baris:
				file.write(row)
				
	else:
		print('Pilih menu 1 sebelum mengcopy data ke file baru!')
	
if __name__ == '__main__':
	main()
