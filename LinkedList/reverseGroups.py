





def reverseGroups(node: Node, k: int):
    curr = node
    prevFirst: Node = node
    isFirstPass: bool = True
    while curr is not None:
        first: Node = curr
        prev = None
        count = 0
        while curr is not None and count < k:
            next = curr.nextNode
            curr.nextNode = prev
            prev = curr
            curr = next
            count += 1
        if isFirstPass:
            node = prev
            isFirstPass = False
        else:
            prevFirst.nextNode = prev
        prevFirst = first
    return node
    
    
    
    
    
    
    
