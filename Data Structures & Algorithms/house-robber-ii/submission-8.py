class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        def dfs(start, end):
            cache = [-1] * len(nums)

            def rob(i):
                if i < start:
                    return 0

                if cache[i] != -1:
                    return cache[i]

                cache[i] = max(
                    rob(i - 1),
                    rob(i - 2) + nums[i]
                )

                return cache[i]

            return rob(end)

        return max(
            dfs(0, len(nums) - 2),  # Include first, exclude last
            dfs(1, len(nums) - 1)   # Exclude first, include last
        )