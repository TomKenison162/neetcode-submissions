class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            return False
        
        # If they match here, great! Otherwise, look left and look right.
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True
        if not p or not q or p.val != q.val: 
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
