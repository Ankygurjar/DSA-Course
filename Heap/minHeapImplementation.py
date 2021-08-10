class MinHeap:
    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.arr: list = [0] * capacity
        self.size: int = 0

    def getLeft(self, i):
        return (2 * i) + 1

    def getRight(self, i):
        return (2 * i) + 2

    def getParent(self, i):
        return (i - 1) // 2

    def insert(self, data: int):
        if self.size == self.capacity:
            return
        self.size += 1
        self.arr[self.size - 1] = data
        i = self.size - 1
        while i != 0 and self.arr[self.getParent(i)] > self.arr[i]:
            temp = self.arr[i]
            self.arr[i] = self.arr[self.getParent(i)]
            self.arr[self.getParent(i)] = temp
            i = self.getParent(i)


def heapify(arr, i):
    lt = (i * 2) + 1
    rt = (i * 2) + 2
    size = len(arr)
    smallest = i
    if lt < size and arr[lt] < arr[i]:
        smallest = lt
    if rt < size and arr[rt] < arr[smallest]:
        smallest = rt
    if smallest != i:
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        heapify(arr, smallest)


ob = MinHeap(10)
arr = [10, 30, 40, 20, 35, 100, 70, 60, 80, 32]
for i in range(len(arr)):
    heapify(arr, i)

for i in range(len(arr)):
    ob.insert(arr[i])

print(arr == ob.arr)
