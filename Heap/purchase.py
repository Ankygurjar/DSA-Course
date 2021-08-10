



def minHeapify(arr, n, i):
    lt = (i * 2) + 1
    rt = (i * 2) + 2
    smallest = i
    if lt < n and arr[lt] < arr[smallest]:
        smallest = lt
    if rt < n and arr[rt] < arr[smallest]:
        smallest = rt
    if smallest != i:
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        minHeapify(arr, n, smallest)


def purchase(arr, sum):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        minHeapify(arr, n, i)
    res = 0
    for i in range(n):
        if arr[i] <= sum:
            sum -= arr[i]
            res += 1
            minHeapify(arr, n, i)
    print(res)


purchase([1, 12, 5, 3, 1, 0, 200], 200)










