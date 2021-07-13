def insertSortedToList(node: Node, data: int):
    if node is None:
        return
    temp = node
    newNode = Node(data)
    if data < node.data:
        newNode.nextNode = temp
        Display(newNode)
        return
    prev = None
    while temp and data > temp.data:
        prev = temp
        temp = temp.nextNode

    prev.nextNode = newNode
    newNode.nextNode = temp
    return node
