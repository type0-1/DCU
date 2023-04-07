class MP3Track(object):

	def __init__(self, title, duration, artists):
		self.title = title
		self.duration = duration
		self.artists = artists

	def __str__(self):
		output = []
		output.append(f'Title: {self.title}')
		output.append(f'By: {", ".join(self.artists)}')
		output.append(f'Duration: {self.duration}')
		return "\n".join(output)