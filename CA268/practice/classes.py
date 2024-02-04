# Classes:

class Person(object):
    def __init__(self, name, age, weight): # Special method "init" that uses attributes 
        self.name = name
        self.age = age
        self.weight = weight
    
    # Methods:

    def show_name(self):
        if hasattr(self.name): # Has and get attr uses object manipulation
            return getattr(self.name)
            
    def show_age(self):
        return self.age
    
    def show_weight(self):
        return self.weight
    
# Inheritance:

class WeightScaler(Person):
    
    def determine_weight(self):
        if self.show_weight() > 70: # Inherits from "Person" class.
            return "Overweight"
        return "Not overweight"
    
# Objects:

person1 = Person("John", 18, 67) 
weight1 = WeightScaler(person1.name, person1.age, person1.weight)

# Print Statement:

print(weight1.determine_weight())

# Polymorphism (A single function, operation etc that can perform multiple tasks):

n1, n2 = 1, 2
n3 = n1 + n2
print(f'{n3} | {type(n3)}')

n1, n2 = "1", "2"
n3 = n1 + n2
print(f'{n3} | {type(n3)}')

