"""
Stack Class
Samson Oloruntola
DSA.

"""

class Stack(object):
    
    def __init__(self):
        items = []
    
    def push(self, e):
        self.items.append(e)

    def pop(self):
        self.items.pop(-1)

    def length(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0
    
