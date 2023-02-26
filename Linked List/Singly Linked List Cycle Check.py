class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def cycle_check(node):
    seen = set()

    while node and node.next:
        if node in seen:
            return True
        else:
            seen.add(node)
            node = node.next

    return False


# Sol 2
def cycle_check2(node):
    marker1 = node
    marker2 = node

    while marker2 is not None and marker2.next is not None:
        marker1 = marker1.next
        marker2 = marker2.next.next

        if marker2 == marker1:
            return True

    return False


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

print(cycle_check(a))
print(cycle_check2(a))

x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z

print(cycle_check(x))
print(cycle_check2(x))
