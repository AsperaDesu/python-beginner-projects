makanan = "bakso"
harga = 18000
print("%s satu porsi harganya %i Rupiah" % (makanan.title(),harga))
harga_dollar = harga / 14500
print("%s satu porsi harganya %i Rupiah atau %.3f Dollar Amerika" % (makanan, harga, harga_dollar))

print()
print("Harga {0:s} adalah {1:d} Rupiah, dalam nilai pecahan {2:f} Rupiah dan {3:2.f} dalam Dollar Amerika".format(makanan, harga, harga, harga_dollar))

