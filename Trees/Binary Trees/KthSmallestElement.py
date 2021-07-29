




def KthSmallestElement(self, root, K): 
    #code here.
    arr = []
    self.getArrayOfNodes(root, arr)
    return arr[K - 1] if K <= len(arr) else -1
    
def getArrayOfNodes(self, tree: Node, arr: list):
    if tree is None:
        return
    self.getArrayOfNodes(tree.left, arr)
    arr.append(tree.data)
    self.getArrayOfNodes(tree.right, arr)


















