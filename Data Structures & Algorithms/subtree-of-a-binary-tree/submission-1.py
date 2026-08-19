# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            elif (not p and q) or (not q and p):
                return False
            if p.val != q.val:
                print(p.val, q.val)
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        if not root and not subRoot:
            return True
        elif (not root and subRoot) or (not subRoot and root):
            return False
     
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or isSameTree(root, subRoot)