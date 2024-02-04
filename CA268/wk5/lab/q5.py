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

    def reverse_string(self, string):
        for c in string:
            self.push(c)
        while self.items != []:
            print(self.pop())

def main():
    s = Stack()
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s.reverse_string(string)


if __name__ == "__main__":
    main()