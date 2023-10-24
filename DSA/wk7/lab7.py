class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
node1 = Node(2)
head.next = node1
node2 = Node(3)
node1.next = node2
node3 = Node(4)
node2.next = node3
node3.next = None

tmp = head

while tmp != None:
    tmp2 = tmp.data
    tmp.data = tmp.next.data
    tmp.next.data = tmp2
    tmp = tmp.next.next

while head != None:
    print(head.data)
    head = head.next