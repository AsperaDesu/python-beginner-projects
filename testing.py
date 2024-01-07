class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def move(self, x, y):
		self.x += x
		self.y += y
		
	def reset(self):
		self.x = 0
		self.y = 0
		
	def __add__(self, other):
		if isinstance(other, Point):
			return self.x + other.x, self.y + other.y
		else:
			return self.increment(other)
		
		
	def __radd__(self, other):
		return self.__add__(other)

	def increment(self, other):
		return self.x + other, self.y + other

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	
	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		
		return self.x, self.y
	
	def __str__(self):
		return f'x : {self.x} | y : {self.y}\n'
	
def main():
	point1 = Point(3, 4)
	point2 = Point(2, 5)
	
	print(point1, point2)
	
	point1 += point2
	print(type(point1))
	print(point1, point2)
	
if __name__ == '__main__':
	main()
