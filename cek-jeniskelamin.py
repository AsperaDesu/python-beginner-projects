print("Menentukan Panggilan Sesuai Jenis Kelamin")
print("-"*30)

kelamin = input("Jenis Kelamin? ")

if kelamin.lower() == "pria" or kelamin.lower() == "laki-laki":
    print(f"""Panggilan untuk seorang {kelamin.title()}
--->Bapak
--->Tuan
--->Bang
--->Mas
""")
elif kelamin.lower() == "perempuan" or kelamin.lower() == "wanita":
    print(f"""Panggilan untuk seorang {kelamin.title()}
--->Ibu
--->Nyonya
--->Kakak
--->Mbak    
""")