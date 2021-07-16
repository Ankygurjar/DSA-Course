







def LeftView(root):

    queue = []
    leftView = []
    queue.append(root)
    flag = False
    while queue :
        size = len(queue)
        for _ in range(size):
            node = queue.pop(0)
            if node:
                if flag == False:
                    leftView.append(node.data)
                    flag = True
                node.left and queue.append(node.left)
                node.right and queue.append(node.right)
        flag = False
    
    return leftView

















