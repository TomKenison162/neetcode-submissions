from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        @lru_cache(None)
        def dfs(i, w):
            
            if w == total-w:
                return True
            if i == len(nums):
                return False
            return dfs(i+1, w + nums[i]) or dfs(i+1, w)
           
            
        
        return dfs(0,0)




        