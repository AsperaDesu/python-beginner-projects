jawaban = set()

print('''+----------------+
| JENIS HIMPUNAN |
+----------------+''')

#SET A
menu = ('1. Lima Bilangan Cacah Pertama ', '2. Lima Bilangan Asli Pertama ', '3. Lima Bilangan Ganjil Pertama', '4. Lima Bilangan Genap Pertama', '5. Lima Bilangan Prima Pertama', '6. Lima Huruf Abjad Pertama', '7. Lima Huruf Vokal ', '8. Lima Huruf Konsonan Pertama ')
for pilihan in menu[:4]:
	print(pilihan)

print()
setA = int(input('>>> SET A, Jenis? '))
print()

while setA > 4:
	setA -= 4

print(setA)

option1 = menu[int(setA) - 1]
option1 = option1[3:].replace('Lima ', '').replace('Pertama', '')

setA = str(setA)


if setA == '1':
	set1 = [i for i in range(5)]
	
elif setA == '2':
	set1 = [i for i in range(1, 6)]
	
elif setA == '3':
	set1 = [i for i in range(1, 10, 2)]

else:
	set1 = [i for i in range(2, 10, 2)]

set1 = tuple(set1)
jawaban.add(set1)


#SET B  
set2 = set()
alphabets =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for pilihan in menu[4:8]:
	print(pilihan)

print()
setB = int(input('>>> SET B, Jenis? '))
print()

if setB < 5:
	setB += 1

else:
	while setB > 8:
		setB -= 4

setB = str(setB)

if setB == '5':
	total = 0
	prima = set()
	
	for j in range(2, 15):
		if total == 5: 
			break
		
		for i in range(2, 15):
			if j % i == 0:
				break
		
		if j == i: 
			prima.add(i)
			total += 1
	
	set2 = prima
	
elif setB == '6':
	fivealpb = alphabets[:5]
	set2 = fivealpb
	
elif setB == '7':
	vokal = [i for i in alphabets if i in 'AIUEO']
	set2 = vokal
	
elif setB == '8':
	consonants = [i for i in alphabets if i not in 'AIUEO']
	fivecons = consonants[:5]
	set2 = fivecons
	
option2 = menu[int(setB) - 1]
option2 = option2[3:].replace('Pertama', '').replace('Lima ', '')
print(option2)
print()

print('SET A', option1 + '->', end = ' ')
print(*set1, sep = ', ')

print('SET B', option2 +  '->', end = ' ')
print(*set2, sep = ', ')
