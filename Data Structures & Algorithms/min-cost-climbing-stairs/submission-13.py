from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        @lru_cache(None)
        def dfs(i):
            if i == 0 or i ==1:
                return min(cost[0] + dfs(2) , cost[1] + min(dfs(2), dfs(3)))
            if i > len(cost)-1:
                return 0
            if i == len(cost)-1:
                return cost[i]

            return cost[i] + min(dfs(i+1), dfs(i+2))
        return dfs(0)
       