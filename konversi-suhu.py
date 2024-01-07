c = -20
i = 0

print("-----------------------------------------------")
print("No.	Celcius  	Fahrenheit	Reumer")
print("-----------------------------------------------")
while i < 25:
	i += 1
	fah = 9/5 * c + 32
	reu = 4/5 * c
	print("%3d	%7d 	%10.2f	%6.2f" % (i, c, fah, reu))
	c += 5
