class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        index ={}
        res = []
        idx = 0
        for x in strs:
            tmp =x
            x = ''.join(sorted(x))

            if x in index:
                res[index[x]].append(tmp)
            else:
                index[x] = idx
                res.append([tmp])
                idx +=1
        return res
                
            



