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

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Call function
head = remove(head, 3)

# Print result

tmp = head

while tmp.next != None:
    print(tmp.data)
    tmp = tmp.next
print(tmp.data)
