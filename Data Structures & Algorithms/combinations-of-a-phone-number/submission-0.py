class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        sub = []
        def dfs(i, val):
            if i   >= len(digits):
                res.append(val)
                return
         

            a,b= 3,0
        
            if  int(digits[i]) == 7 or int(digits[i]) ==9:
                a += 1
            if int(digits[i]) ==8 or int(digits[i]) ==9:
                b =1
            
            for j in range(0,a):
                e= chr(97 + (int(digits[i])-2)* 3 + b + j)
                dfs(i+1, val + e)
        
        dfs(0, "")
        if res == [""]:
            return []
        return res




