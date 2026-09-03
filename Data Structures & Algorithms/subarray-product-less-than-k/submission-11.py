class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:      
        if k <= 1:
            return 0
        start, end = 0,0
        res = 1
        prod = nums[0]
        
        while end +1 < len(nums):
            end +=1
            prod *= nums[end] 
            while prod >= k:
                prod //= nums[start]
                start += 1 
            res += end-start +1
        return res
            
                
            
            
         