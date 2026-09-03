class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        t, c = nums[0], nums[0]

        for num in nums[1:]:
            #print(num, c ,t)
            c = max(num, c + num)
            t = max(t, c)
            
        return t