class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ", "")
        s = s.lower()
        f, l = 0, len(s)-1
        while f < l:
            while not s[f].isalnum() and f < l:
                f +=1
            while not s[l].isalnum() and f < l:
                l -= 1
            if s[f] != s[l]:
                return False
            f +=1
            l -= 1
        return True 