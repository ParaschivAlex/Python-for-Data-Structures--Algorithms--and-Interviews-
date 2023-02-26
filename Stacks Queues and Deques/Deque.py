class Deque:
    def __init__(self):
        self.deque = []

    def addFront(self, item):
        self.deque.insert(0, item)

    def addRear(self, item):
        self.deque.append(item)

    def removeFront(self):
        return self.deque.pop(0)

    def removeRear(self):
        return self.deque.pop()

    def isEmpty(self):
        return self.deque == []

    def size(self):
        return len(self.deque)


test = Deque()
test.addRear(1)
test.addFront(2)
test.addRear(3)  # 2 1 3
print(test.deque)

print(test.removeFront())  # 1 3
print(test.deque)

test.addFront(4)
test.addFront(5)  # 5 4 1 3
print(test.removeRear())  # 5 4 1
print(test.deque)

print(test.size())

print(test.isEmpty())
test.deque = []
print(test.isEmpty())
