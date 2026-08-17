# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def explore(tree, maxi):
    if tree == None:
        return maxi
    dia = height(tree.left) + height(tree.right)

    return max(explore(tree.left, max(maxi,dia)), explore(tree.right, max(maxi,dia)))

def height(tree):
    if tree == None:
        return 0

    return max(height(tree.left), height(tree.right)) +1
       
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return explore(root, 0)


        