class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0] *n 
        def dfs(i):
            print(i, cache)
            if i == 0:
                cache[i] = 1
                return 1
            if i ==1:
                cache[i] =2
                return 2
            if cache[i] != 0:
               return cache[i]
            cache[i] = dfs(i-1) + dfs(i-2)
            return cache[i]
        dfs(n-1)
        return cache[-1]
            
        