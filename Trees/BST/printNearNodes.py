







def printNearNodes(self, root, low, high):
    #code here.
    arr = []
    self.inOrder(root, arr, low, high)
    return arr
    
def inOrder(self, tree, arr, low, high):
    if tree is None:
        return
    self.inOrder(tree.left, arr, low, high)
    if tree.data >= low and tree.data <= high:
        arr.append(tree.data)
    self.inOrder(tree.right, arr, low, high)
    
    
    
    
    
    
    
    
    
