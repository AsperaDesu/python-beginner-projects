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

for product in products:		
	for key, value in product.items():
		print(f'{key.title():12} : {value}')
	print()
