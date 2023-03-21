class Stack(object):

	def __init__(self):
		self.l = []

	def push(self, s):
		self.l.append(s)

	def pop(self):
		return self.l.pop()

	def top(self):
		return self.l[-1]

	def is_empty(self):
		return len(self.l) == 0

	def __len__(self):
		return len(self.l)