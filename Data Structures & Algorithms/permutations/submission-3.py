class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(first):
            # Base Case: All positions have been filled
            if first == len(nums):
                res.append(nums.copy())
                return
            
            for i in range(first, len(nums)):
                # Place nums[i] at the current 'first' position
                nums[first], nums[i] = nums[i], nums[first]
                
                # Recurse for the remaining positions
                dfs(first + 1)
                
                # Backtrack: Restore the original array state
                nums[first], nums[i] = nums[i], nums[first]
                
        dfs(0)
        return res
