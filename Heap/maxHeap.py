def maxHeapify(arr, i):
    lt = (i * 2) + 1
    rt = (i * 2) + 2
    largest = i
    size = len(arr)
    if lt < size and arr[lt] > arr[i]:
        largest = lt
    if rt < size and arr[rt] > arr[largest]:
        largest = rt
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        maxHeapify(arr, largest)


arr = [10, 15, 50, 4, 20]

for i in range(len(arr)):
    maxHeapify(arr, i)

print(arr)
