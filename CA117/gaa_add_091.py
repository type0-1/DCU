class Score():
	def __init__(self, goals=0, points=0):
		self.goals = goals
		self.points = points

	def scoreConversion(self):
		return (self.goals * 3) + self.points

	def __add__(self, other):
		total_goals = self.goals + other.goals
		total_points = self.points + other.points
		return Score(total_goals, total_points)

	def __iadd__(self, other):
		self.goals += other.goals
		self.points += other.points 
		return self
		
	def __str__(self):
		return "{} goal(s) and {} point(s)".format(self.goals, self.points)


