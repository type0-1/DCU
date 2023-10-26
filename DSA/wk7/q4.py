class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def swap_pairs(head):

    new_head = head.next
    tmp = head

   


	
    return new_head

head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

head.next = n2
n2.next = n3 
n3.next = n4

head = swap_pairs(head)

while head:
    print(head.data)
    head = head.next
