import random

simpan = ""

angka1 = random.randrange(1, 7)
angka2 = random.randrange(1, 7)

kali = 1

while True:
	
	dadu1 = 0
	dadu2 = 0
	
	while (dadu1 < 1 or dadu1 > 6):			
		dadu1 = int(input("Silahkan tebak Mata Dadu 1? "))
		
		if dadu1 < 1 or dadu1 > 6:
			print("---Isikan Tebakan Mata Dadu Dari 1 s/d 6!!\n")
		
	while (dadu2 < 1 or dadu2 > 6):
		dadu2 = int(input("Silahkan tebak Mata Dadu 2? "))
		
		if dadu2 < 1 or dadu2 > 6:
			print("---Isikan Tebakan Mata Dadu Dari 1 s/d 6!!\n")
	
	if dadu1 == angka1 and dadu2 != angka2:
		print("---> Mata Dadu 2 Salah!!")

	elif dadu1 != angka1 and dadu2 == angka2:
		print("--->Mata Dadu 1 Salah!")

	elif dadu1 != angka1 and dadu2 != angka2:
		print("---> Mata Dadu 1 dan 2 Salah!")
	
	else:
		print("Tepat Sekali.")
		print(f"Anda Membutuhkan {kali} kali untuk mendapatkan mata dadu yang benar!")
		break
	
	print("-" * 35)
	print("Tebakan Sebelumnya")
		
	simpan = simpan + f"	{kali}. Mata Dadu 1 = {dadu1} dan Mata Dadu 2 = {dadu2}\n"
	print(simpan)
		
	print("\n")
	 
	kali += 1
