class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        cache = [-1] * len(nums)

        def dfs(i):
            print(cache, nums, i)
            if i < 2:
          
                cache[i] = max(nums[0], nums[i])  
        
                return cache[i]


            if cache[i] != -1:
                return cache[i]
           
            one = dfs(i-1)
            if i == len(nums) -1:
                cache[1:] = [-1] * (len(nums)-1)
                nums[0] =-2
            two = max(0,dfs(i-2)) + nums[i]
            if one > two:
                cache[i] = one
            else:
                cache[i] = two
                

           
            return cache[i]
        dfs(len(nums)-1)
        print(cache)
        return max(cache[-1], cache[-2])
        