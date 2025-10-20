def get_num(prompt : str, data_type = int, start = None, end = None):
	while True:
		try:
			num = int(input(prompt).strip())
			if start is not None:
				if num < start:
					continue
			if end is not None:
				if num > end:
					continue
			return data_type(num)
		except ValueError:
			continue

def yesOrNo(prompt : str):
	answer = 'a'
	while answer != 'y' and answer != 't':
		answer = input(prompt).lower().strip()
		
	return answer
