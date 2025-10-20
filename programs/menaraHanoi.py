def main():
	print('=' * 25)
	print('MENARA HANOI'.center(25))
	print('=' * 25, '\n')
	
	jmlh = int(input('Jumlah Piringan? '))
	txt = hanoi(jmlh, 'A', 'B', 'C')
	print(txt)
	
def hanoi(n, a, b, c):
    if n == 1:
        return(f"Pindahkan piring 1 dari {a} ke {c}\n")
    
    txt1= hanoi(n-1, a, c, b)
    txt2 = (f"Pindahkan piring {n} dari {a} ke {c}\n")
    return txt1 + txt2 + hanoi(n-1, b, a, c)

if __name__ == '__main__':
	main()
