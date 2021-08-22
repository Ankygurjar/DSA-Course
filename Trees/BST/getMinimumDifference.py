

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minVal = float('inf')
        arr = self.getInorderArr(root, [])
        for i in range(0, len(arr)-1):
            minVal = min(minVal, abs(arr[i] - arr[i+1]))
        return minVal
        
    def getInorderArr(self, tree, arr):
        if tree is None:
            return 
        self.getInorderArr(tree.left, arr)
        arr.append(tree.val)
        self.getInorderArr(tree.right, arr)
        return arr






