class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def assign():
    tmp = head
    for i in range(2, 6):
        current = Node(i)
        tmp.next = current
        tmp = current
        
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

head = Node(1)
assign()
head = remove(head, 5)
tmp = head

while tmp.next != None:
    print(tmp.data)
    tmp = tmp.next

print(tmp.data)
