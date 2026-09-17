# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        current = [root, 0]
        res = []
        if root is None:
            return []
        while True:
            
          
            if current[0].left is not None:
                que.append([current[0].left, current[1] +1])
            if current[0].right is not None:
                que.append([current[0].right, current[1] +1])
            if que:
                tmp =que.popleft()
            else:
                res.append(current[0].val)
                break

            if  tmp[1] !=  current[1]:
                res.append(current[0].val)
            current =tmp
        return res




        