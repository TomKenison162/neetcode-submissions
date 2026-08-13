def binary(low, high, target, nums):
        med = (low + high)//2

        if low > high:
            return -1

        if target>nums[med]:
            return binary(med+1, high, target,nums)
        elif target<nums[med]:
            return binary(low, med-1, target,nums)
        else:
            return med

class Solution:


        
    def search(self, nums: List[int], target: int) -> int:
        x = binary(0, len(nums)-1, target, nums)
        return x
    
   