class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next = b
b.previous = a

b.next = c
c.previous = b
