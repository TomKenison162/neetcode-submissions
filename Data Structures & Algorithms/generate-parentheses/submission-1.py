class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def valid(stri):
            count = 0
            for i in range(len(stri)):
                if stri[i] == "(":
                    count += 1
                else:
                    count -= 1
            return count
       
        res = []
        def dfs(i, current):
            if i >= n*2:
                # TWEAK 1: Only collect strings that perfectly balanced out to 0
               
                res.append(current)   
                return
            
            # TWEAK 2: Allow adding "(" if open count hasn't hit 'n' yet
            # (We count total "(" by adding length and balance together, then dividing by 2)
            if (len(current) + valid(current)) // 2 < n:
                dfs(i+1, current + "(")
                
            # TWEAK 3: Allow adding ")" only if there is an open "(" waiting to be closed
            if valid(current) > 0:
                dfs(i+1 , current + ")")
                
            return
        dfs(0, "")
     
        return res
