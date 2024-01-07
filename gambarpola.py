def main():
	print('''MENGGAMBAR DAN MENYIMPAN
Silahkan gambar di bawah ini menggunakan keyboard!!!
-----------------------------------------------------------''')

	destination = input("Nama file yang ingin dibaca? ")
	
	print()
	
	masukan = 'a'
	string = []
	while masukan != '':
		masukan = input("? ")
		string.append(masukan + '\n')
		
	string.pop()
	
	with open(destination, 'w') as f:
		for line in string:
			f.write(line)
	
	print(f'Layar berhasil disimpan ke "{destination}"')
	
if __name__ == '__main__':
	main()		
	
