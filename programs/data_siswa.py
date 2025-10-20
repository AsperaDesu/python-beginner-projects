import math

menu = ('A. Membaca Data', 'B. Extract Data', 'C. Menampilkan Per Siswa', 'D. Menampilkan Tabel Siswa', 'E. Menambahkan Data', 'F. Mengedit Data', 'G. Menghapus Data', 'H. Mengurutkan Data', 'I. Menyimpan Data', 'Z. Keluar')

def main():
		with open('datasiswa.txt', 'r+') as f:
			data = None
			max_char = 13
			student_dict = None
			
			while True:

				print('<<< M E N U >>>\n---------------')
				print(*menu, sep = '\n')
				print()

				masukan = input("Pilihan Anda? ").lower().strip()
				print()
				

				match masukan:
					case 'a':
						data = read_data(f)
						print(data)
						
					case 'b':
						if data == None:
							print('Maaf, extract data tidak bisa dilakukan karena data belum dibaca!!!')
						else:
							student_dict, headers = extract_data(data)
							print(student_dict)
							extracted = True
							
					case 'c':
						if validate(student_dict):
							per_student(student_dict, max_char)
							
					case 'd':
						if validate(student_dict):
							student_table(student_dict, max_char, headers)
						
					case 'e':
						if validate(student_dict):
							max_char, student_dict = add_data(student_dict, max_char, headers, f)
					
					case 'f':
						if validate(student_dict):
							student_dict = edit_data(student_dict, max_char, headers)
					
					case 'g':
						if validate(student_dict):
							student_dict = erase_data(student_dict, headers, max_char)
					
					case 'h':
						if validate(student_dict):
							student_dict = sort_data(student_dict, headers, max_char)
					
					case 'i':
						if validate(student_dict):
							f.close()
							write_data(student_dict, headers)
						
						f = open('datasiswa.txt', 'r+')
						
					case 'z':
						break
				
				print('\n')
				print('-' * 50)
				
			
			
			
def read_data(f):
		print("Sedang membaca data...")
		print('Membaca data selesai!\n')	
	
		print('Data yang dibaca dari file >>>>>')
		f.seek(0)
		
		return f.readlines()
			
			
def extract_data(data):
		print('Sedang mengextract data...')
		print('Extract data selesai!!!')
		print()
		
		print('Hasil setelah data di-extract >>>>')
		header = []
		
		headers = data[0].split(',')
		headers[-1] = headers[-1].rstrip()
		dicts = {}
		temp = {}
		
		for value in data[1:]:
			temp = {}
			value = value.split(',')
			value[-1] = value[-1].rstrip()
			for i in range(1, len(headers)):
				if value[i].isdigit():
					value[i] = int(value[i])
				temp[headers[i]] = value[i]
			dicts[value[0]] = temp
		
		return dicts, headers



def per_student(data, limit):
	print('Hasil setelah data ditampilkan per siswa >>>>>')
	
	for identity, information in data.items():
		print_data(identity, information, limit)
		
		print()
	


def student_table(data, limit, headers):
	limit += limit * 0.5
	lines = (limit-1) * len(headers)
	limit = math.ceil(limit)
	lines = math.ceil(lines)
	
	#<<<<<<<<<JUDUL>>>>>>>>
	print('Hasil setelah data ditampilkan dalam tabel >>>>')
	print('-' * lines)
	
	print(f'{"ID":<{limit}}', end = '')
	
	for i in headers[1:]:
		print(f'{i.title():<{limit}}', end = '')
	print()

	print('=' * lines)
	
	#--------------------------------------------
	#<<<<<<<<<<<DATA>>>>>>>>>
	
	for identity, value in data.items():
		print(f'{identity:<{limit}}', end = '')
		
		for keys in headers[1:]:
				print(f'{value[keys]:<{limit}}', end = '')
		print()
		
	print('-' * lines)
	
	#----------------------------------------------
	
	

def add_data(data, limit, headers, f):
	print('Menambahkan data >>>>')
	confirm = 'y'	
		
	while confirm == 'y':
		identity = input('ID? ')
		temp = {}
		
		if identity in data:
			print('>>> ID siswa sudah pernah diisikan!')
			continue
		
		for i in headers[1:]:
			temp[i] = input(f'{i.title()}? ').title()
			if temp[i].isdigit():
				temp[i] = int(temp[i])
			
			if len(str(temp[i])) > limit:
				limit = len(temp[i])
		
		data[identity] = temp
		
		print()
		confirm = input('Input lagi [Y/T]? ').lower()
	
	print(data)
	
	return limit, data
		
		
		
def edit_data(data, limit, headers):
	print('Mengedit data >>>>')
	confirm = 'y'
	
	while confirm != 't':
		identity = input('ID? ')
		if identity in data:
			print('Data Siswa Sekarang:')
			print_data(identity, data[identity], limit)
			
			print()
			
			print('Data Siswa Baru (Enter berarti tidak diubah!!!')
			print(f'{"ID":<{limit}} : {identity}')
			
			temp = {}
			for key in headers[1:]:
				masukan = input(f'{key:<{limit}} ? ').title()
				if masukan.isdigit():
					masukan = int(masukan)
				
				if masukan != '':
					temp[key] = masukan
				else:
					temp[key] = data[identity][key]
			
			data[identity] = temp
		
		else:
			print('>>>ID Siswa tidak ditemukan!')
			continue
			
		confirm = input('\nEdit lagi [Y/T]? ').lower()
	
	return data
	
	
def erase_data(data, headers, limit):
	print('Menghapus data >>>>')
	confirm = 'y'
	deleted = False
	
	while confirm == 'y':
		identity = input('ID? ')

		if identity in data:
			print('Data Siswa Sekarang:')
			print_data(identity, data[identity], limit)
			
			confirm_del = input('Siswa dihapus [Y/T]? ').lower()
			print('\n')
			
			if confirm_del == 'y':
				del data[identity]
				print(f'>>>Siswa dengan ID: {identity} berhasil dihapus!!!\n')
				deleted = True
				
			confirm = input('Hapus lagi [Y/T]? ').lower()
			
		else:
			print('>>>ID Siswa tidak ditemukan!')
	
	if deleted:
		print('Hasil setelah data dihapus >>>>')
		print(data)
	
	return data
	


def sort_data(data, headers, limit):
	print('Mengurutkan data >>>>>>')
	print(data)
	print()
	print('Urutkan data menurut:')
	
	convert = {}
	
	for num, i in enumerate(headers, start = 1):
		print(f'{num}. {i.title()}')
		convert[num] = i
	
	print()
	sorts = input('Pilihan anda (Tambahkan "r" untuk urut terbalik)? ')
	print()
	
	sorting, reverse = split_data(sorts)
	sorting = convert[sorting]
	
	reverse_value = False
	
	if reverse == 'r':
		reverse_value = True

	if sorting == 'id':
		data = sorted(data.items(), key = lambda x:x, reverse = reverse_value)
	elif sorting == 'nama':
		data = sorted(data.items(), key = lambda x:x[1][sorting], reverse = reverse_value)
	else:
		data = sorted(data.items(), key = lambda x: (x[1][sorting], x[1]['nama']), reverse = reverse_value)
	
	print('Hasil setelah data diurutkan >>>>')
	print(data)
	
	return dict(data)
	
	
def write_data(data, headers):
	with open('datasiswa.txt', 'w+') as f:
		print('Menyimpan data >>>>')
		f.write(','.join(headers) + '\n')
		rows = []
		
		for ids, info in data.items():
			row = ids 
			for keys in headers[1:]:
				row += ',' + str(info[keys])
			rows.append(row)
			
		print(rows)
		f.writelines('\n'.join(rows))
		
		print()
		print('Data selesai disimpan!!')
		
	
	
def split_data(x):
	number = ''
	char = ''
	for i in x:
		if i.isdigit():
			number += i
		else:
			char += i
	
	return int(number), char


def validate(data):
	if data == None:
		print('Maaf, perintah tidak bisa dilakukan karena data belum di extract!!!')
		return False
	
	return True
	
def print_data(identity, data, limit):
	
	print(f'{"ID":<{limit}} : {identity}')
	for key, value in data.items():
		print(f'{key.title():<{limit}} : {value}')

if __name__ == '__main__':
	main()
