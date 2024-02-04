"""
Week 4:
Author: Samson Oloruntola
Queue Implementation in Python

First in, first out. (FIFO)

"""

class Queue(object):

    def __init__(self):
        self.queue = []
    
    def enqueue(self, n):
        self.queue.insert(0, n)
    
    def dequeue(self):
        return self.queue.pop() if len(self.queue) > 0 else f'Error!'
    
    def is_empty(self):
        return len(self.queue) == 0

    def first(self):
        return self.queue[0]
    
    def __len__(self):
        return len(self.queue)

def main():
    Q = Queue()
    Q.enqueue(5) # contents : [5]
    Q.enqueue(3) # contents : [5 , 3]
    print(len(Q)) # output : 2
    print(Q.dequeue()) # contents : [3]; output : 5
    print(Q.is_empty()) # output : False
    Q.dequeue() # contents : []; output : 3
    print(Q.is_empty()) # output : True
    print(Q.dequeue()) # Error !
    Q.enqueue(7) # contents : [7]
    Q.enqueue(9) # contents : [7 , 9]
    print(Q.first()) # contents : [7 , 9]; output : 7
    Q.enqueue(4) # contents : [7 , 9 , 4]
    print(len(Q)) # output : 3
    Q.dequeue()

if __name__ == "__main__":
    main()