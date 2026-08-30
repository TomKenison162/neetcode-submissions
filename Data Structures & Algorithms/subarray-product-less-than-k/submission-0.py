class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        s = 0
        prod = 1
        res = 0
        for i in range( len(nums)):
            
            prod  *= nums[i]
            
            while s <= i  and prod >= k:
                prod //=nums[s]
                s+=1
            res += (i - s +1)
        return res
            
                
            
            
         