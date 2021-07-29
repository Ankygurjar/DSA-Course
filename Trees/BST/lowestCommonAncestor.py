








def LCA(root, n1, n2):
    #code here.
    if root is None:
        return
    if n1 > root.data and n2 > root.data:
        return LCA(root.right, n1, n2)
    if n1 < root.data and n2 < root.data:
        return LCA(root.left, n1, n2)
    return root














