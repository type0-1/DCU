class Student():

	def __init__(self, sid, name, modlist=None):
		self.sid = sid
		self.name = name
		self.modlist = modlist or []

	def add_module(self, add):
		if add not in self.modlist:
			self.modlist.append(add)

	def del_module(self, delete):
		if delete not in self.modlist:
			self.modlist.remove(delete)

	def __str__(self):
		return f'ID: {self.sid}\nName: {self.name}\nModules: {", ".join(sorted(self.modlist))}'

