class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        cache = [-1] * len(nums)

        def dfs(i):

            if i < 2:
                cache[i] = max(nums[0], nums[i])  
                return cache[i]


            if cache[i] != -1:
                return cache[i]

            cache[i] = max(dfs(i-1), dfs(i-2) + nums[i])
            return cache[i]
        dfs(len(nums)-1)
        print(cache)
        return max(cache[-1], cache[-2])
        