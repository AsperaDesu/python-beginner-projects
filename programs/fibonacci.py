print("--------------------")
print("Barisan FIBONACCI")
print("-------------------")

suku = int(input("Tampilkan Sampai Suku Ke? "))

prev = 0
total = 0
now = 1
i = 0 

while i < suku:
	print(now, end = "  ")
	total = prev + now
	prev = now 	
	now = total
	i += 1 
