# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
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
                res.append(node.val)
                prev = stack.pop()
            
        return res