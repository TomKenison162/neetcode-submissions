class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        dp = [0] * (len(nums)+1)
        def dfs(i, w):
            if i == len(nums):
                return False
            if w == total-w:
                return True
            return dfs(i+1, w + nums[i]) or dfs(i+1, w)
           
            
        
        return dfs(0,0)




        