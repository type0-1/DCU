def getMinutes(duration):
	return divmod(duration, 60)

class MP3Track(object):

	def __init__(self, title, duration, artists):
		self.title = title
		self.duration = duration
		self.artists = artists

	def __str__(self):
		minutes, seconds = getMinutes(self.duration)
		output = []
		output.append(f'Title: {self.title}')
		output.append(f'By: {", ".join(self.artists)}')
		output.append(f'Duration: {minutes:01d}:{seconds:02d}')
		return "\n".join(output)
