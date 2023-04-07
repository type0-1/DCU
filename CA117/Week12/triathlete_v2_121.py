class Triathlete(object):

	def __init__(self, name, tid):
		self.name = name
		self.tid = tid
		self.time = {}

	def add_time(self, discipline, time):
		self.time[discipline] = time

	def get_time(self, discipline):
		return self.time[discipline]

	def race_time(self):
		total = sum([time for time in self.time.values()])
		return total

	def __str__(self):
		output = []
		output.append(f'Name: {self.name}')
		output.append(f'ID: {self.tid}')
		output.append(f'Race time: {self.race_time()}')
		return "\n".join(output)
