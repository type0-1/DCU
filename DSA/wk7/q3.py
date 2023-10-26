"""
Author: Samson Oloruntola
Question: Reverse the Linked-List recursively.
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def recursion(head, prev=None):

    curr = head

    if curr is None:
        return prev

    tmp = curr.next
    curr.next = prev
    prev = curr
    curr = tmp
    
    return recursion(curr, prev)

# Node assignment

head = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)

head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

# Assign new head

head = recursion(head)

# Print result

while head:
    print(head.data)
    head = head.next
