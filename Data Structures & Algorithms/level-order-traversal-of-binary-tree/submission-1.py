# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = [[]]

        def dfs(index, root):
            if root == None:
                return

            res[index].append(root.val)
            res.append([])
            dfs(index+1, root.left)
            dfs(index +1, root.right)
        dfs(0, root)
        fin = []
        for i in res:
            if i != []:
                fin.append(i)

        return fin
        