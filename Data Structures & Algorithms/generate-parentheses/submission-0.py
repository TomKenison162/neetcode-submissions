class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def valid(stri):
            count = 0

            for i in range(len(stri)):
                if stri[i] == "(":
                    count +=1
                else:
                    count -=1
                    if count < 0:
                        return False
            return count == 0
       
        res = []
        def dfs(i, current):
            print(i, current)
            if i >= n*2:
                if valid(current):
                    res.append(current)
               
                    
                return
          
            dfs(i+1, current + "(")
            dfs(i+1 , current + ")")
        dfs(0, "")
        print(res)
        return res

                
                
        