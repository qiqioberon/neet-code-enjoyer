# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mD(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 1
        left = self.mD(root.left)
        right = self.mD(root.right)
        return max(res+left, res+right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        left = self.mD(root.left)
        right = self.mD(root.right)
        if abs(left-right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)