class Stack:
    """
    Python implementation the stack
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
    
    def letter_sequence(self, string):
        inner = []
        for c in string:
            if c != "*":
                inner.append(c)
            else:
                self.push(inner.pop())


## Sample inputs
if __name__ == '__main__':
    s = Stack()
    string = 'EAS*Y*QUE***ST***IO*N***'
    s.letter_sequence(string)
    print(s.items)
