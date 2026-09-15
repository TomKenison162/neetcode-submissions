from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        grid = [[-1] * (sum(nums)+1) for _ in range(len(nums)+1)]
        @lru_cache(None)
        def dfs(t, i):
        
            if i == len(nums):
                if t == target:
                    return 1
                else:
                    return 0
            
            if i > len(nums):
                return 0
            
            
            grid[i][t] = dfs(t - nums[i], i+1) + dfs(t + nums[i], i +1)
            return grid[i][t]
        res = dfs(0,0)
 
        return res
        