
#NEEDS TO BE OPTIMIZED


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        px = self.getParent(root, x, None)
        py = self.getParent(root, y, None)
        xLevel = self.getLevel(root, x)
        yLevel = self.getLevel(root, y)
        return True if px != py and xLevel == yLevel else False
    
    def getLevel(self, tree, val):
        queue = []
        queue.append(tree)
        level = 0
        while queue:
            size = len(queue)
            for i in range(0, size):
                cur = queue.pop(0)
                if cur.val == val:
                    return level+1
                cur.left and queue.append(cur.left)
                cur.right and queue.append(cur.right)
            level += 1
                    
    
    def getParent(self, tree, val, prev):
        if tree is None:
            return
        if tree.left and tree.left.val == val:
            return tree.val
        if tree.right and tree.right.val == val:
            return tree.val
        else:
            return self.getParent(tree.left, val, tree) or self.getParent(tree.right, val, tree)
                
        









