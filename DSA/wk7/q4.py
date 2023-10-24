class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def assign():
    tmp = head
    for i in range(1, 10):
        current = Node(i)
        tmp.next = current
        tmp = current



tmp = head

while tmp != None:
    tmp2 = tmp.data
    tmp.data = tmp.next.data
    tmp.next.data = tmp2
    tmp = tmp.next.next

while head != None:
    print(head.data)
    head =  head.next