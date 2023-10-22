"""
Week 4:
Author: Samson Oloruntola
Stack Implementation in Python.

First in, last out. (FILO)
"""

class Stack(object):

    def __init__(self):
        self.stack = []
    
    def push(self, e):
        self.stack.append(e)
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)
    
def main():
    S = Stack()
    S.push(5) # contents : [5]
    S.push(3) # contents : [5 , 3]
    print(len(S))
    print(S.pop()) # contents : [5]; output : 3
    print(S.is_empty()) # output : False
    print(S.pop()) # contents : []; output : 5
    print(S.is_empty()) # output : True
    S.push(7) # contents : [7]
    S.push(9) # contents : [7 , 9]
    print(S.top()) # contents : [7 , 9]; output : 9
    S.push(4) # contents : [7 , 9 , 4]
    print(len(S))
    print(S.pop()) # contents : [7 , 9]; output : 4
    S.push(6) 
if __name__ == "__main__":
    main()