"""
Author: Samson Oloruntola
Question: Assign Nodes in two's from 0-100 to Linked List.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(0)
tmp = head

for i in range(2, 104, 2):
    current = Node(i)
    tmp.next = current
    tmp = current

while head.next != None:
    print(head.data)
    head = head.next