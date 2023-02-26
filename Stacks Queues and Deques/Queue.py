class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)


test = Queue()
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
print(test.queue)

print(test.dequeue())
print(test.queue)

test.enqueue(4)

print(test.queue)
print(test.size())

print(test.isEmpty())
test.queue = []
print(test.isEmpty())
