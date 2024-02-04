class Queue:
    """
    Python implementation the queue
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def binary_sequence(self, n):
        for i in range(n, 0, -1):
            self.enqueue(int(bin(i)[2:]))
        


if __name__ == '__main__':
    q = Queue()
    q.binary_sequence(16)
    print(q.items)
    print(q.dequeue())
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())
    print(q.size())
