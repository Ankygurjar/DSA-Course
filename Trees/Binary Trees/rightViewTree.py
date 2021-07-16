










class Solution:
    def rightView(self,root):
        rightView = []
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node:
                    if i+1 == size:
                        rightView.append(node.data)
                    node.left and queue.append(node.left)
                    node.right and queue.append(node.right)
        
        return rightView













