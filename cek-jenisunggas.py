print("Memeriksa Jenis Unggas")
print("-"*30)

terbang = input("""Apakah unggas bisa terbang?
--->[BT=Bisa Terbang | TT=Tidak Bisa Terbang]. Jawaban Anda? """)
selaput = input("""Apakah jari kaki unggas ada selaput?
--->[AS=Ada Selaput | TS=Tidak Ada Selaput]. Jawaban Anda? """)

tt = "Tidak Bisa Terbang"
bt = "Bisa Terbang"
aS = "Ada Selaput"
ts = "Tidak Ada Selaput"

terbang = terbang.lower()
selaput = selaput.lower()

if terbang == "tt" and selaput == "ts":
    ket = tt
    ket2 = ts
    unggas = "AYAM"
elif terbang == "bt" and selaput == "ts":
    ket = bt
    ket2 = ts
    unggas = "BURUNG"
elif terbang == "bt" and selaput == "as":
    ket = bt
    ket2 = aS
    unggas = "BELUM DIKETAHUI JENISNYA"
else:
    ket = tt
    ket2 = aS
    unggas = "BEBEK"

print(f"""Kesimpulan:
--->Unggas {ket}
--->Unggas {ket2}
--->Jenis Unggas yang dimaksud adalah {unggas}
""")