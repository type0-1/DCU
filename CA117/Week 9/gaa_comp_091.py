class Score():
	def __init__(self, goals=0, points=0):
		self.goals = goals
		self.points = points

	def scoreConversion(self):
		return (self.goals * 3) + self.points

	def __str__(self):
		return "{} goal(s) and {} point(s)".format(self.goals, self.points)

	def __gt__(self, other):
		return self.scoreConversion() > other.scoreConversion()

	def __eq__(self, other):
		return self.scoreConversion() == other.scoreConversion()
		
	def __le__(self, other):
		return self.scoreConversion() <= other.scoreConversion()


