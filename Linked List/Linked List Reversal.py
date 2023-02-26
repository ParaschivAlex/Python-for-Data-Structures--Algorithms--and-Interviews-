class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(node):
    current = node
    previous = None
    nextn = None

    while current:
        nextn = current.next
        current.next = previous
        previous = current
        current = nextn

    return previous


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

reverse(a)

print(d.value)
print(d.next.value)
print(c.next.value)
print(b.next.value)
