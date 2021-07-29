








def getCount(root,low,high):
    ##Your code here
    arr = []
    getNum(root, arr, low, high)
    return  len(arr)
    
def getNum(root, arr, low, high):
    if root is None:
        return 
    getNum(root.left, arr, low, high)
    if root.data >= low and root.data <= high:
        arr.append(root.data)
    getNum(root.right, arr, low, high)















