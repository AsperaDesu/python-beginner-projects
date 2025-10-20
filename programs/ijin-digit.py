print("Membalikkan Nilai Digit")
print("---------------------------")

digit = ""
while not digit.isdigit():		
	digit = input("Isikan Sebuah DIGIT? ")
else:
	digit = digit[len(digit)::-1]
	print("Yang diisikan berisi DIGIT semua, DIGIT akan dibalikkan!")
	print(f"---> DIGIT Setelah Dibalik: {digit}")
