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

    def letter_sequence(self, string):
        inner = []
        for c in string:
            if c != "*":
                inner.insert(0, c)
            else:
                self.enqueue(inner.pop())
        self.items = self.items[::-1]


if __name__ == '__main__':
    q = Queue()
    string = 'EAS*Y*QUE***ST***IO*N***'
    q.letter_sequence(string)
    print(q.items)