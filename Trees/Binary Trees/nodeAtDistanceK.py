






def nodeAtDistanceK(head: TreeNode, k: int):
    if head is None:
        return

    if k == 0:
        print(head.data)

    distanceK(head.left, k - 1)
    distanceK(head.right, k - 1)



















