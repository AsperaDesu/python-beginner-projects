products = [{
'kode' : 1,
'nama produk' : 'Pensil',
'harga satuan' : 2000,
'merk produk' : 'Faber-Castell'},
{'kode' : 2,
'nama produk' : 'Pena',
'harga satuan' : 7000,
'merk produk' : 'Joyko'},
{'kode' : 3,
'nama produk' : 'Pensil',
'harga satuan' : 1800,
'merk produk' : 'Joyko'}]

sample = {
'nama produk' : 'Pena',
'harga satuan' : 7000,
'merk produk' : 'Joyko'}

totalProduct = 3
pilih = '1'

while pilih != '0':
	for i in range(len(products)):
		products[i]['kode'] = '%.5d' % (int(products[i]['kode'] ))

	print('-' * 60)

	for key in products[0]:
		print(key.title(), end = '     ')

	print('\n' + '=' * 60)
		
	for product in products:
		for key, value in product.items():
			print(str(value).ljust(len(key) + 5), end = '')
		print()

	print('-' * 60) 

	print('\n')

	print('''<<< PRODUK  INVENTORY >>>
1. Menambahkan Produk
2. Mengedit Produk
3. Menghapus Produk
4. Mengurutkan Produk
5. Menambahkan Key Produk 
6. Menghapus Key Produk
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
			
		print()
