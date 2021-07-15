






def maxiMum(head: TreeNode):
    if head is None:
        return -float("inf")

    return max(head.data, max(maxiMum(head.left), maxiMum(head.right)))


def miniMum(head: TreeNode):
    if head is None:
        return float("inf")

    return min(head.data, min(miniMum(head.left), miniMum(head.right)))

















