"""

Week 2 - Notes.
Author: Samson Oloruntola
Date: 18/09/2023

:-> Object Manipulation <-:

setattr(object, attribute, value) -> sets the value with attribute
 
getattr(object, attribute, value) -> returns the value
 
delattr(object, attribute, value) -> deletes the attribute

hasattr(object, attribute, value) -> checks if the attribute exists in the object.


Polymorphism:

The ability for an attribute, method or variable to have multiple functionalities.

Encapsulation:

Protected variables: ("_"variable_name) -> is a way of sending the message to other developers. 
"Variable is protected". (Don't use variable outside its scope).

"__"variable-name = "Private variable". Can't be used outside the scope.


"""

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def is_student(self): # Method 1:
        return False


class Student(Person):

    def is_student(self):  # Method 2: Inherits from the "Person" class, a form of polymorphism, returning a different value .
        return True

person1 = Person("Tom", 19)
student1 = Student("Jack", 18)
print(student1.is_student())

