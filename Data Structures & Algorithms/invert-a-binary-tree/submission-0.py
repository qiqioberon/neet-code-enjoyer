# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = root
        stack = []
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack[-1]
            if node.right and prev != node.right:
                root = node.right
            else:
                temp = node.right
                node.right = node.left
                node.left = temp
                prev = stack.pop()
        return res

