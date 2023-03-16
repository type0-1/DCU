class Student(object):
   def __init__(self, name, uid, modules, average=0):
      self.name = name
      self.uid = uid
      self.modules = modules
      self.average = average

   def getAverage(self):
      self.average = round((self.modules[0][1] + self.modules[1][1]) / 2)
      return self.average

   def __str__(self):
      self.modules = sorted(self.modules)
      output = []
      output.append(f'Name: {self.name}')
      output.append(f'ID: {self.uid}')
      output.append(f'Modules: {self.modules[0][0]}, {self.modules[1][0]}')
      output.append(f'Average mark: {self.average}')
      return "\n".join(output)

class Classlist(object):
   def __init__(self):
      self.dic = {}

   def add(self, other):
      self.dic[other.getAverage()] = other

   def __str__(self):
     output = []
     for k, v in sorted(self.dic.items(), reverse=True):
        output.append(f'{v}')
     return "\n".join(output)
