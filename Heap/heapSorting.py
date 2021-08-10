






def maxHeapify(arr, n, i):
    lt = (i * 2) + 1
    rt = (i * 2) + 2
    largest = i
    if lt < n and arr[lt] > arr[largest]:
        largest = lt
    if rt < n and arr[rt] > arr[largest]:
        largest = rt
    if largest != i:
        temp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = temp
        maxHeapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        maxHeapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        maxHeapify(arr, i, 0)

    return arr


print(heapSort([10, 15, 50, 4, 20]))














