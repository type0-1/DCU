class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def swap_pairs(head):

    new_head = head.next
    
    prev = head
    curr = head.next

    while curr:
        
        prev.next = curr.next
        curr.next = prev
        tmp = prev.next
        prev = tmp

        if tmp is None:
            curr = tmp
            break

        curr = tmp.next

        head.next = curr
        head = curr


    
    return new_head

head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

head.next = n2
n2.next = n3 
n3.next = n4
n4.next = n5
n5.next = n6

head = swap_pairs(head)

while head:
    print(head.data)
    head = head.next
