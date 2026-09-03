class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        dp = [[[0] * rows] for _ in range(cols)]

        directions = [[1,0], [-1, 0], [0,1], [0,-1]]
        
        def dfs(i, j):
            
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0":
                return 0
         
            grid[i][j] = "0"
            

            for d in directions:
                dfs(i+d[0], j+d[1])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count +=1
                   

        return count
        
        