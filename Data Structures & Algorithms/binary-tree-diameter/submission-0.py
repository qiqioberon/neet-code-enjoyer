# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(res+left, res+right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left+right, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))