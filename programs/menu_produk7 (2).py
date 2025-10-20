products = [{
'kode' : 1,
'nama produk' : 'Pensil',
'harga satuan' : 2000,
'jml stok' : 100,
'merk produk' : 'Faber-Castell'},
{'kode' : 2,
'nama produk' : 'Pena',
'harga satuan' : 7000,
'jml stok' : 150,
'merk produk' : 'Joyko'},
{'kode' : 3,
'nama produk' : 'Pensil',
'harga satuan' : 1800,
'jml stok' : 275,
'merk produk' : 'Joyko'}]

sample = {
'nama produk' : 'Pena',
'harga satuan' : 7000,
'merk produk' : 'Joyko'}

totalProduct = 3
pilih = '1'

hide = False
opt7 = '7. TAMPILKAN HARGA X STOK'

while pilih != '0':
	
	for i in range(len(products)):
		products[i]['kode'] = '%.5d' % (int(products[i]['kode'] ))
	
	kali = 0
	for i in products[0].keys():
		kali += len(i) + 5
	
	print('-' * kali)

	for key in products[0]:
		print(key.title(), end = '      ')

	print('\n' + '=' * kali)
		
	for product in products:
		for key, value in product.items():
			if str(value).isnumeric() and key != 'kode':
				print(str(value).rjust(len(key)), end = '      ')
			else:
				print(value.ljust(len(key) + 6), end = '')
		print()

	print('-' * kali) 

	print('\n')

	print(f'''<<< PRODUK  INVENTORY >>>
1. Menambahkan Produk
2. Mengedit Produk
3. Menghapus Produk
4. Mengurutkan Produk
5. Menambahkan Key Produk 
6. Menghapus Key Produk
{opt7}
0. Keluar
	''')

	pilih = input('Pilihan Anda? ')
	print()
	
	if pilih == '1':
		print('Menambahkan Produk >>>')
		finished = False
		
		while not finished:
			new = {}
			
			totalProduct += 1 
			
			new['kode'] = '%.5d' % (totalProduct)
			print('Kode:',new['kode'])
			
			for key in products[0]:
				if key !='kode':
					new[key] = input(f'{key.title().strip()}? ').title()
					if new[key] == '':
						totalProduct += -1
						finished = True
						break
			
			if not finished:
				products.append(new)
			print()
			
	elif pilih == '2':
		print('Mengedit Produk >>>')
		edit = int(input('Kode yang diedit? '))
		print()
		
		if totalProduct >= edit:
			print('<Produk ditemukan>')
			for key, value in products[edit  - 1].items():
				print(f'{key.title()}: {value}')
			
			print('\nProduk DIEDIT menjadi:')
			for key, value in products[edit  - 1].items():
				if key == 'kode':
					print('Kode:', value)
				
				else:
					change = input(f'{key.title()}: {value}	---> ').title()
					
					if change != '':
						products[edit -1][str(key)] = str(change)
				
		else:
			print('<Kode yang dicari tidak ditemukan!>')
		
	elif pilih == '3':
		print('Menghapus Produk >>>')
		erase = int(input("Kode yang dihapus? "))
		print()
		
		if totalProduct >= erase:
			print('<Produk ditemukan>')
			
			for key, value in products[erase  - 1].items():
				print(f'{key.title()}: {value}')
			
			print()
			confirm = input('Produk DIHAPUS [Y/T]? ').upper().strip()
			print(f'Posisi = {erase -1}')
			print()
			
			if confirm == 'Y':
				del products[erase - 1]
				print('Produk berhasil dihapus!')
				totalProduct += -1
				
				
			elif confirm == 'T':
				print('Produk tidak jadi dihapus!')
			
		else:
			print("<Kode yang dicari tidak ditemukan!>")

	elif pilih == '4':
		print("<<<SUB MENU MENGURUTKAN PRODUK>>>")
		number = 0
		
		pilihan = {}
		
		for i in products[0]:
			number += 1
			print(f'{number}. {i.title()}')
			pilihan[str(number)] = i
		
		print('0. Keluar\n')
		
		pilih2 = input('Pilihan Anda? ')
		
		if pilih2 != '0':
			urut = pilihan[pilih2]
			print('Urutkan --->', urut.title())
			nomor = 0
			
			newprod = {}
			
			for i in products:
				nomor += 1
				newprod[nomor] = i
			
			sort = sorted(newprod.items(), key = lambda x: x[1][urut])
			
			for i in range(len(products)):
				products[i] = sort[i][1]
			
	elif pilih == '5':
		print('Menambahkan Key Produk >>>')
		newInv = input('Key Produk Baru? ').lower().strip()
		
		print()
		
		if newInv in products[0]:
			print('Key tersebut sudah ada!')
				
		else:
			
			for i in range(len(products)):
				print('Produk:')	
				
				for k, v in products[i].items():
					print(f'{str(k).title()}:  {str(v).title()}')
				
				products[i][newInv] = input(f'{newInv.title()}? ')
				print()
		
	elif pilih == '6': 
		print('Menghapus Key Produk >>>')
		keyHapus = 'kode'
		
		while keyHapus == 'kode':
			keyHapus = input("Key Produk yang dihapus (kecuali: Kode)? ").lower()
		
		if keyHapus not in products[0].keys():
			print(f'Maaf, Key Produk yang dihapus {keyHapus} tidak ditemukan!')
		
		else:
			print('Terhapus!')
			for i in products:
				del i[keyHapus]
			
	elif pilih == '7':
		
		if hide:
			opt7 = '7. TAMPILKAN HARGA X STOK' 
			hide = False
		
			try:
				for i in products:
					del i['Harga X Stok']
		
			except KeyError:
				pass
				
		else:
			opt7 = '7. TIDAK TAMPILKAN HARGA X STOK'
			hide = True
			
			for i in products:
				try:
					i['Harga X Stok'] = int(i['harga satuan']) * int(i['jml stok'])
					
				except KeyError:
					if 'harga satuan' in products[0].keys():
						print('Key "Jml Stok" tidak ditemukan')
					elif 'jml stok' in products[0].keys():
						print('Key "Harga Satuan" tidak ditemukan')
					else:
						print('Key "Harga Satuan" dan "Jml Stok" tidak ditemukan')

					break 
						
	print()	
		
