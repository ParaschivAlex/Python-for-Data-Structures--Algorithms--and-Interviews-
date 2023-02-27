class BinaryHeap(object):  # minHeap
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def swapUp(self, i):
        while i:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i //= 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.swapUp(self.currentSize)

    def findMin(self):
        return self.heapList[1]

    def percDown(self, i):

        while (i * 2) <= self.currentSize:

            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minChild(self, i):

        if i * 2 + 1 > self.currentSize:

            return i * 2
        else:

            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def isEmpty(self):
        return self.currentSize == 0

    def size(self):
        return len(self.heapList)

    def buildHeap(self, nodes):
        i = len(nodes) // 2
        self.currentSize = len(nodes)
        self.heapList = [0] + nodes[:]
        while i:
            self.percDown(i)
            i = i - 1


t = BinaryHeap()
t.buildHeap([14, 11, 18, 19, 21, 33, 17, 27, 9, 5])
print(t.heapList)