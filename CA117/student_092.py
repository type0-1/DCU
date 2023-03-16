class Student(object):
   def __init__(self, name, uid, modules):
      self.name = name
      self.uid = uid
      self.modules = modules

   def getAverage(self):
      for mark in self.modules:
         print(mark)

   def __str__(self):
      self.modules = sorted(self.modules)
      average = round((self.modules[0][1] + self.modules[1][1]) / 2)
      output = []
      output.append(f'Name: {self.name}')
      output.append(f'ID: {self.uid}')
      output.append(f'Modules: {self.modules[0][0]}, {self.modules[1][0]}')
      output.append(f'Average mark: {average}')
      return "\n".join(output)
