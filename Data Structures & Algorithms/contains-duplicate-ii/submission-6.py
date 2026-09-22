
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        w = set()
        L =0
        for i in range(len(nums)):
            if i - L > k:
                w.remove(nums[L])
                L +=1
            if nums[i] in w:
                return True
            w.add(nums[i])
        return False
