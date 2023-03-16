import math

class Point():
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def distance(self, point):
		return math.sqrt(((((self.x - point.x) ** 2)) + ((self.y - point.y) ** 2)))


	def __str__(self):
		return f'({self.x:.1f}, {self.y:.1f})'