class Cal():
	def __init__(self, first, second):
		self.first = first
		self.second = second
	def sum(self):
		return self.first + self.second

cal1 = Cal(1,2)
print(cal1.sum())