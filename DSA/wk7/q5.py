"""
Author: Samson Oloruntola
Question: Remove N'th Node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
   
def remove(head, n):

    tmp = head

    if n == 1:
        return head.next
    
    i = 2

    while i != n:
        i+=1
        tmp = tmp.next

    tmp.next = tmp.next.next
    
    return head

# Node Assignment:

head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

# Connect Nodes

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

# Call function

head = remove(head, 6)

# Print result

tmp = head

while tmp != None:
    print(tmp.data)
    tmp = tmp.next
