class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def pal(strs):
            return strs == strs[::-1]
        sub = []
        agg = []
        def dfs(i):
                
            if i >= len(s):
                agg.append(sub.copy())
                return
            for j in range(i, len(s)):
                 if pal(s[i:j+1]):
                    sub.append(s[i : j + 1])
                    dfs(j + 1)
                    sub.pop()
        dfs(0)
        return agg
