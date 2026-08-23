class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        cache = [0] *len(cost)
        def dfs(i):
            if i == 0:
                cache[i] = cost[i]
                return cache[i]
            if i == 1:
                cache[i] = cost[i]
                return cache[i]
            if cache[i] !=0:
                return  cache[i]
            cache[i] = min(dfs(i-1), dfs(i-2)) + cost[i]
            return  cache[i]
        dfs(len(cost)-1)
        return min(cache[-1], cache[-2])
            

            
