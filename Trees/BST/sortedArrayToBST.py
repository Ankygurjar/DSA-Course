


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 1:
            return TreeNode(nums[0])
        return self.addToBst(nums, 0, len(nums)-1)
    
    def addToBst(self, nums, l, r):
        if l > r:
            return None
        mid = l + (r - l)//2
        node = TreeNode(nums[mid])
        node.left = self.addToBst(nums, l, mid - 1)
        node.right = self.addToBst(nums,  mid+1, r)
        return node







