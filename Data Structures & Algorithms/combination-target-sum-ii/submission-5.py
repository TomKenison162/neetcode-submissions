class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        aggre = []
        subset = []
        def dfs(i, total):
            if total > target:
                return
            if i >= len(candidates):
                if total ==target:
                    aggre.append(subset.copy())
                return
            if total ==target:
                aggre.append(subset.copy())
                return
            subset.append(candidates[i])
            dfs(i+1, total+ candidates[i])
            subset.pop()
            n = 1
            while  i +n < len(candidates) and candidates[i] == candidates[i+n]:
                n +=1
            dfs(i+n, total)
        dfs(0, 0)
        return aggre
        