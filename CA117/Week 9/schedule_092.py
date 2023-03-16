class Meeting():
	def __init__(self, hour, minute, duration):
		self.hour = hour
		self.minute = minute
		self.duration = duration

	def __str__(self):
		return f'{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)'

class Schedule():
	def __init__(self):
		self.dic = {}

	def add(self, other):
		self.dic[other.hour] = other

	def __str__(self):
		lists = []
		print("Schedule")
		print("--------")
		for k, v in (sorted(self.dic.items())):
			lists.append(f'{v}')
		lists.sort()
		lists.append(f'Meetings today: {len(lists)}')
		return "\n".join(lists)