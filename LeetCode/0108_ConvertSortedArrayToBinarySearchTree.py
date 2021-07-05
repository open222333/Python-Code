# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = len(nums) // 2  # 取中間值
        ans = TreeNode(nums[mid])
        leftSide = nums[:mid]
        rightSide = nums[mid + 1:]
        ans.left = self.sortedArrayToBST(leftSide)
        ans.right = self.sortedArrayToBST(rightSide)
        return ans
