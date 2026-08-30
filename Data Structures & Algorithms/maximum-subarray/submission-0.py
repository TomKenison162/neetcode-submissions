class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        gmax = cmax = nums[0]

        for num in nums[1:]:
            cmax = max(num, cmax + num)
            gmax = max(gmax, cmax )
        return gmax
        