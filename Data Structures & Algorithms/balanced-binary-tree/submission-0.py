# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def explore(tree, balance):
            if tree == None:
                return 0, balance
            left, b1 = explore(tree.left, balance) 
            right, b2 = explore(tree.right, balance)
            if not b1 or not b2:
                balance = False
            if -1 <= (left -  right) <= 1:
                return max(left, right) +1, balance
            else:
                return 0, False
        
        _, truth = explore(root, True)
        return truth
                
                 

        
        