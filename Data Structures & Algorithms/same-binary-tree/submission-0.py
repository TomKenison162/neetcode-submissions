# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def explore(tree1, tree2):
            if tree1 == None and tree2 == None:
                return True
            elif tree1 == None or tree2 == None:
                return False
            elif tree1.val != tree2.val:
                return False
            return explore(tree1.left, tree2.left) and explore(tree1.right, tree2.right)
        return explore(q, p)