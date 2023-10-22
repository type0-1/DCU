"""
Week 4:
Author: Samson Oloruntola
Deque (Double-Ended Queues) Implementation in Python.

First in, both first and last out??

"""

class Deque(object):

    def __init__(self):
        self.deque = []
    
    def add_last(self, n):
        self.deque.append(n)
    
    def add_first(self, n):
        self.deque.insert(0, n)
    
    def first(self):
        return self.deque[0]

    def delete_last(self):
        return self.deque.pop(-1)
    
    def last(self):
        return self.deque[-1]

    def __len__(self):
        return len(self.deque)
    
    def is_empty(self):
        return len(self.deque) == 0
    

def main():
    D = Deque()
    D.add_last(5) # contents : [5]
    D.add_first(3) # contents : [3 , 5]
    D.add_first(7) # contents : [7 , 3 , 5]
    print(D.first()) # output : 7
    D.delete_last() # contents : [7 , 3]; output : 5
    print(len(D)) # output : 2
    print(D.delete_last()) # contents : [7]; output : 3
    print(D.delete_last()) # contents : []; output : 7
    D.add_first(6) # contents : [6]
    print(D.last()) # output : 6
    D.add_first(8) # contents : [8 , 6]
    print(D.is_empty()) # output : False
    D.last()

if __name__ == "__main__":
    main()