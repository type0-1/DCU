class Queue(object):

	def __init__(self):
		self.l = []

	def enqueue(self, s):
		self.l.insert(0, s)

	def dequeue(self):
		return self.l.pop()

	def first(self):
		return self.l[-1]

	def is_empty(self):
		return len(self.l) == 0

	def __len__(self):
		return len(self.l)
