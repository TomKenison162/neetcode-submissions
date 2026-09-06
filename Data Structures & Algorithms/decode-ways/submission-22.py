from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] =="0":
            return 0

  
        @lru_cache(None)
        def dfs(i):
            if i >= len(s):
                return 1
            if i == len(s)-1:
                if s[i] == "0":
                    return 0
                if s[i] != "0":
                    return 1
                else:
                    return 0
           
            if int(s[i:i+2]) <= 26:
                if s[i] == "0":
                    return 0
                
                if s[i+1] !="0":
                    return  (dfs(i+1)) + (dfs(i +2))
                else:
                    return dfs(i +2)
            else:
                if s[i] != "0":
                    return  dfs(i+1)
                else:
                    return 0
        val = dfs(0)
        return val
