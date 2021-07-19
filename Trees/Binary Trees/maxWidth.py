




    def getMaxWidth(self,root):
       
        #code here
        if root is None:
            return 0
        queue = []
        maxWidth = 0
        queue.append(root)
        while queue:
            size = len(queue)
            maxWidth = max(maxWidth, size)
            for _ in range(size):
                node = queue.pop(0)
                node.left and queue.append(node.left)
                node.right and queue.append(node.right)
        return maxWidth



















