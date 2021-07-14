








def segregateEvenOddNodes(node: Node):
    newList = Node(None)
    even = newList
    cur: Node = node
    prev: Node = None
    while cur and cur.nextNode:
        if cur.data % 2 == 0:
            even.nextNode = Node(cur.data)
            even = even.nextNode
            temp = cur.nextNode
            prev = cur
            cur.data = temp.data
            cur.nextNode = temp.nextNode
        else:
            prev = cur
            cur = cur.nextNode
    if cur != None and cur.data % 2 == 0 and prev.data != cur.data:
        even.nextNode = Node(cur.data)
        even = even.nextNode
        prev.nextNode = prev.nextNode.nextNode
    even.nextNode = node
    Display(newList.nextNode)















