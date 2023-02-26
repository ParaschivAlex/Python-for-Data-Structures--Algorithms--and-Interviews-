class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self) -> int:
        # popped = self.stack[-1]
        # del self.stack[-1]
        # return popped
        return self.stack.pop()

    def peek(self) -> int:
        # return self.stack[-1]
        return self.stack[len(self.stack)-1]

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


# test = Stack()
# test.push(1)
# test.push(2)
# test.push(3)
# print(test.stack)
#
# print(test.pop())
# print(test.stack)
#
# test.push(4)
# print(test.peek())
#
# print(test.size())
#
# print(test.isEmpty())
# test.stack = []
# print(test.isEmpty())

