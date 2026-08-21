class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        current = []
        subset =[]
        dicts = {}
        

        def dfs(i):
            if i>= len(candidates):
                if sum(subset) == target:
                    count = dicts.get(str(sorted(subset)), -1)
                    if count == -1:
                        current.append(subset.copy())
                        dicts[str(sorted(subset))] =1
                    
                return 
            subset.append(candidates[i])
            dfs(i +1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return current