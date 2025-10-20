products = {
'kode' : 1,
'nama produk' : 'Pensil',
'harga satuan' : 2000,
'merk produk' : 'Faber-Castell'}

products['kode'] = '%.5d' % (products['kode'] )

for key, value in products.items():
	print(f'{key.title():12} : {value}')
