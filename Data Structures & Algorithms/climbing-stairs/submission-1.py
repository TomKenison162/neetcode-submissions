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
           
            if cache[i-1] != 0:
                one = cache[i-1]
            else:
                one =  dfs(i-1)
            if cache[i-2] != 0:
                two = cache[i-2]
            else:
                two= dfs(i-2)
            cache[i] = one +two
            return cache[i]
        dfs(n-1)
        return cache[-1]
            
        