# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def invert_child(tree):
    if tree == None:
        return None
    return TreeNode(tree.val, invert_child(tree.right), invert_child(tree.left) )
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return invert_child(root)
        