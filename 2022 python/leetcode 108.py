class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return
        idx=len(nums)//2
        root=TreeNode(nums[idx])
        root.left=self.sortedArrayToBST(nums[:idx])
        root.right=self.sortedArrayToBST(nums[idx+1:])
        return root

s=Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9]))