print("-" * 30)
print("JUMLAH BILANGAN-BILANGAN".center(30))
print("-" * 30)

print("""1. Bilangan Asli
2. Bilangan Ganjil
3. Bilangan Genap
4. Bilangan Kelipatan x
5. Bilangan Fibonacci x y
6. Keluar""")

while True:
	print()
	pilihan = input("Pilihan Anda? ").strip()
	print()
	
	if pilihan in "1 2 3 4 5":
		ulang = int(input("Jumlah Perulangan? "))
		if pilihan == "1":
			for i in range(1, ulang + 1):
				total = 0
				for j in range(1, i+1):
					if j < i:
						print(f"{j} + ", end = "")
					else:
						print(f"{j}", end = "")
					total += j
				print(f" = {total}")
					
		elif pilihan == "2":
			for i in range(ulang):
				total = 0
				for j in range(i + 1):
					if j < i:
						print(f"{(j*2)+1} + ", end = "")
					else:
						print(f"{(j*2)+1}", end = "")
					total += (j * 2) + 1
				print(f" = {total}")
				
		elif pilihan == "3":
			for i in range(ulang):
				total = 0
				for j in range(i + 1):
					if j < i :
						print(f"{(j * 2) + 2} + ", end = "")
					else:
						print(f"{j * 2 +2}", end = "")
					total += j * 2 + 2
				print(f" = {total}")
					
		elif pilihan == "4":
			kelipatan = int(input("Kelipatan Dari? "))	
			for i in range(1, ulang + 1):
				total = 0
				for j in range(i + 1):
					total = j * kelipatan
				print(total, end = " ")
			print()
			
		else:
			print()
			x = 1
			y = 0
			while x > y:
				x = int(input("Bilangan Pertama? "))
				y = int(input("Bilangan Kedua? "))
				if x > y:
					print("Bilangan Kedua tidak bisa lebih kecil dari Bilangan Pertama\n")			
			
			print()
			print("Jumlah Bilangan Fibonacci")			
				total = 0
			for i in range(ulang):
				print(x, end = "   ")
				total = x + y
				x = y
				y = total
			print()

	elif pilihan == "6":
		break
	
	while True:
		b = input("Tekan Enter untuk melanjutkan")
		if b == "":
			break

