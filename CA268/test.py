class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


root = Node(15)
root.left = Node(12)
temp = Node(20)

def is_root(temp):
    if temp.val == root.val:
        return True
    return False

print(is_root(temp))