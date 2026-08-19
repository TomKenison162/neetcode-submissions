class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        comp = 0

        for n in nums:
            comp = n ^ comp
        return comp

        