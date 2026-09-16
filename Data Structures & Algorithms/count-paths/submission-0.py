class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * (n+1) for _ in range(m+1)]
        


        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        print(grid)
        return grid[-2][-2]
