class Stack(object):

    def __init__(self):
        items = []

    def is_empty(self):
        return len(self.items) == 0

    def length(self):
        return len(self.items)