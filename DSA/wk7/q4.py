class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def swap_pairs(head):

    new_head = head.next

    prev = head
    curr = head.next

    if new_head.next == None:

        temp = curr.next
        curr.next = prev
        prev.next = temp
        
        return new_head

    while curr:

        temp = curr.next
        curr.next = prev
        prev.next = temp

        head.next = curr
        head = prev
        prev = temp

        if temp is None:
            return new_head

        curr = temp.next

    return new_head

head = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

head = swap_pairs(head)

while head:
    print(head.data)
    head = head.next
