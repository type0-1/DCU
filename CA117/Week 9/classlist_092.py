class Student(object):
    def __init__(self, name, uid, modules, mark=0):
        self.name = name
        self.uid = uid
        self.modules = modules
        self.mark = mark

    def getAverage(self):
        self.mark = round(sum(module[1] for module in self.modules) / len(self.modules))
        return self.mark

    def __str__(self):
        output = []
        self.modules = sorted(self.modules)
        output.append(f'Name: {self.name}')
        output.append(f'ID: {self.uid}')
        output.append(f'Modules: {", ".join([module[0] for module in self.modules])}')
        output.append(f'Average mark: {self.getAverage()}')
        return "\n".join(output)

class Classlist(object):
	def __init__(self):
		self.dic = {}

	def add(self, other):
	   self.dic[other.uid] = other

	def __str__(self):
	   return "\n".join([f'{v}' for k, v in sorted(self.dic.items(), reverse=True)])
