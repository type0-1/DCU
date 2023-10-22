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
    
    def post_fix(self, string):
        operations = ["+","-","*","^","/"]
        for c in string:
            if c not in operations:
                self.push(int(c))
            else:
                b = self.pop()
                a = self.pop()
                tasks = {"+" : a + b, "-" : a - b, "*": a * b, "^": a ** b, "/": a // b}
                result = tasks[c]
                self.push(result)



## Sample inputs
if __name__ == '__main__':
    s = Stack()
    string = "1432^*+147--+"
    s.post_fix(string)
    print(s.items)
