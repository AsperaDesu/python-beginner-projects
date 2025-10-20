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

for i in range(len(products)):
	products[i]['kode'] = '%.5d' % (products[i]['kode'] )

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
0. Keluar''')
