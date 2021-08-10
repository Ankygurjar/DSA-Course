class MinHeap:
    def __init__(self, capacity) -> None:
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        return (index * 2) + 1

    def getRightChildIndex(self, index):
        return (index * 2) + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def insert(self, data):
        if self.isFull():
            raise ("Heap is Full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIdx = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(
                index
            ):
                smallerChildIdx = self.getRightChildIndex(index)
            if self.storage[index] < self.storage[smallerChildIdx]:
                break
            else:
                self.swap(index, smallerChildIdx)

    def removeMin(self):
        if self.size == 0:
            raise ("Heap is Full")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown()

    def display(self):
        print(self.storage)


heap = MinHeap(20)
heap.insert(10)
heap.insert(20)
heap.insert(15)
heap.insert(40)
heap.insert(50)
heap.insert(100)
heap.insert(25)
heap.insert(45)
heap.insert(12)
heap.removeMin()
heap.display()
