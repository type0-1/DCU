"""
Author: Samson Oloruntola
Find reference to first node with same data.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def find(self, data):
        while self != None:
            if self.data == data:
                return self.data
            self = self.next
        return None

head = Node("Dublin")
another_node = Node("Galway")
head.next = another_node
a_third_node = Node("Cork")
another_node.next = a_third_node

result = head.find("Galway")
print(result)