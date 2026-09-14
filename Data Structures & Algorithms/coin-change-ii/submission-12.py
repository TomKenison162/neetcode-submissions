class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[-1]*(amount +1) for _ in range(len(coins) +1)  ]
        if amount == 0:
            return 1
        

        def dfs(i, j):
            if j == amount:

                return 1
            if j > amount:
                return 0
            if i >= len(coins):
                return 0
            
           
            if dp[i][j] != -1:
                return dp[i][j]
           
            dp[i][j] =   dfs(i, j + coins[i]) +  dfs(i +1, j)
            return dp[i][j]
        dfs(0,0)
        
 
        return dp[0][0]

        