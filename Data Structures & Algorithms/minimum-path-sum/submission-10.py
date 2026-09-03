from functools import lru_cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        @lru_cache(None)
        def dfs(i,j):
            if i == rows or j == cols:
                return float("inf")
            if i == rows -1 and j == cols -1:
                return grid[i][j]

            return grid[i][j]+ min(dfs(i+1, j), dfs(i, j+1))
        return dfs(0,0)





        