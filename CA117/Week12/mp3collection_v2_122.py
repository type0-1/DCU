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

class MP3Collection(object):

	def __init__(self):
		self.tracks = {}

	def add(self, track):
		self.tracks[track.title] = track 

	def remove(self, track):
		del self.tracks[track]

	def lookup(self, title):
		return self.tracks[title] if title in self.tracks else None

	def __add__(self, other):
		newInstance = MP3Collection()
		for mp3 in self.tracks.values():
			newInstance.add(MP3Track(mp3.title, mp3.duration, mp3.artists))
		for mp3 in other.tracks.values():
			newInstance.add(MP3Track(mp3.title, mp3.duration, mp3.artists))
		return newInstance
		