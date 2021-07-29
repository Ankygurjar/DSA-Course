






def findPair(root,X):
    # code here 
    mySet = set()
    queue = []
    queue.append(root)
    while queue:
        curNode = queue.pop(0)
        if curNode:
            reqNum = X - curNode.key
            if reqNum in mySet:
                return True
            mySet.add(curNode.key)
        curNode.left and queue.append(curNode.left)
        curNode.right and queue.append(curNode.right)
    
    return False
