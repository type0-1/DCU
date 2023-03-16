class Contact():
	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

	def __str__(self):
		return f'{self.name} {self.phone} {self.email}'


class Contactlist():
	def __init__(self):
		self.d = {}

	def add(self, name):
		self.d[name.name] = name

	def get(self, name):
		if name in self.d:
			return self.d[name]
		return None
	
	def remove(self, name):
		if name in self.d:
			del self.d[name]

	def __str__(self):
		list = []
		list.append("Contact list")
		list.append("------------")
		for k, v in sorted(self.d.items()):
			list.append(f'{v}')
		return "\n".join(list)