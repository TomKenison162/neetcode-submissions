# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def explore(tree):
    if tree == None:
        return 0

    return max(explore(tree.left), explore(tree.right)) +1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return explore(root)
        