class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def nth_to_last_node(n, head) -> int:
    arr = []
    while head:
        arr.append(head)
        head = head.next
    return arr[-n]


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

sol = nth_to_last_node(2, a)
print(sol.value)
