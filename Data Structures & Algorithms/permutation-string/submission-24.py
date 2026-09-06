from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n2 = len(s2)
        n1= len(s1)
        s1 = Counter(s1)
        dict2 = Counter(s2[0:n1])

        if s1 == dict2:
                return True
        
        for i in range(n1, n2):

            dict2[s2[i-n1]] -=1
            if dict2[s2[i-n1]] == 0:
                del dict2[s2[i-n1]]
            dict2[s2[i]] +=1
            if s1 == dict2:
                return True
        return False
