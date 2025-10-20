uang = 120000
pecahan = 50000
bagi = uang//pecahan
sisa = uang % pecahan

print("Besaran Uang?", uang)
print("Pecahan Uang Yand Diinginkan?", pecahan)
print()
print("Besaran uang {0:d} dapat ditukar dengan pecahan {1:d} sebanyak {2:.0f} lembar dan masih mempunyai sisa {3:d} rupiah".format(uang, pecahan, bagi, sisa))

