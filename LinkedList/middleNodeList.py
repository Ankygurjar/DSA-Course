def middle(node: Node):
    if node is None:
        return None
    slow = node
    fast = node.nextNode
    if fast is None:
        return slow.data
    if fast.nextNode is None:
        return fast.data
    while fast and fast.nextNode and fast.nextNode.nextNode:
        slow = slow.nextNode
        fast = fast.nextNode.nextNode
    return slow.nextNode.data if fast is not None else slow.data
