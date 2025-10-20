pilihan = input('Pilihan Anda? ')
nilai = input('Nilai yang diisikan? ')

kunci = [int("'"+str(nilai)+"'",2), 2, int("'" + nilai + "'", 8), 8, int("'" + nilai + "'", 16), 16]

print(kunci[kunci.find(pilihan) - 1])
