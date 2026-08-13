class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict1 = {}
        b,e = 0,0
        maxi = 0
        for i in range(len(s)):

            val = dict1.get(s[i], -1)
            if val == -1:
                dict1[s[i]] = i
            else:
                dict1[s[i]] = i
                b = max(val +1, b)
            e+=1
            maxi = max(maxi, e-b)
        print(e, b, dict1)
        return maxi

            
        
            
        
        