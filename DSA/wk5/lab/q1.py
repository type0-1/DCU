"""
Week 5:
Author: Samson Oloruntola
Question 1:

1: Reversing a Queue.
2: Sort the Queue using Recursion.
3: Reversing for "k" Elements of the Queue.

"""

class Queue(object):

    def __init__(self):
        self.items = []
    
    def enqueue(self, n):
        self.items.insert(0, n)
    
    def dequeue(self):
        self.items.pop()
    
    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0
    
    def reverse(self):
        self.items = self.items[::-1]
    
    # Taken from the solution ( couldn't figure it out )

    def enqueue_conditioned(self, temp, q_size):
        if self.is_empty() or q_size == 0:
            self.items.append(temp)
        return

        elif temp <= self.items[0]:
            self.items.append(temp)
            self.push_to_last(q_size)

        else:
            self.items.append(self.items.pop(0))
            self.enqueue_conditioned(temp, q_size - 1)

    # Taken from the solution ( couldn't figure it out )

    def sort_queue(self):
        if self.is_empty():
            return

        temp = self.items.pop(0)
        self.sort_queue()

        self.enqueue_conditioned(temp, self.size())
        
    def reverse_k(self, k):
        self.items = self.items[:k][::-1] + self.items[k:]

def main():
    q = Queue()
    q.enqueue(13)
    q.enqueue(2)
    q.enqueue(34)
    q.enqueue(43)
    q.enqueue(50)
    print(q.items)
    q.reverse()
    print(q.items)
    """
    print(q.dequeue())
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())
    print(q.size())
    """

if __name__ == "__main__":
    main()


