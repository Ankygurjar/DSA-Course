







def insert(tree: Node, data):
    if tree is None:
        return Node(data)
    elif data > tree.key:
        tree.right = insert(tree.right, data)
    elif data < tree.key:
        tree.left = insert(tree.left, data)
    return tree











