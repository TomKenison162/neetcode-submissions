class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        cache = [0] * len(nums)
        def dfs(i, loot):
            if i < 2:
                cache[i] = max(nums[0], nums[i])   # change 1
                return cache[i]

            if cache[i] != 0:
                return cache[i]

            loot = max(dfs(i-1, loot), dfs(i-2, loot + nums[i]) + nums[i])
            cache[i] = loot
            return loot
        return dfs(len(nums)-1, 0)                 # change 2