class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        for i in range(len(grid)):
           
            for j in range(len(grid[0])):
                print(cache)
                if i == 0 and j==0:
                    cache[i][j] = grid[i][j]
                elif i-1 >=0 and j-1 >=0:
                    cache[i][j] = min(cache[i-1][j], cache[i][j-1]) + grid[i][j]      
                elif i-1 >=0:
                    cache[i][j] = cache[i-1][j] + grid[i][j]
                else:
                     cache[i][j] = cache[i][j-1] + grid[i][j]

        
        return cache[-1][-1] 



        