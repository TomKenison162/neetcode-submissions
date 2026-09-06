# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = []
        def dfs(root):
            if root is None:
                return False
            
            left =dfs(root.left)
            right =dfs(root.right)
            if root == p or root == q:
                
                if left or right:
                    res.append(root)
                    return False
                return True
            if left and right:
                res.append(root)
                return False
            elif left or right:
                return True
        dfs(root)
        return res[0]


        