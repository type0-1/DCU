class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

head.next = n2
n2.next = n3 
n3.next = n4

tmp = head

while tmp.next != None:
    tmp.next.next = tmp
    tmp = tmp.next

while head.next != None:
    print(head.data)
    head = head.next
print(head.data) 