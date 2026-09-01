class Solution:
    def isHappy(self, n: int) -> bool:

        freq ={}
        current = n

        while freq.get(current,-1) == -1:
            
            freq[current] = 1
            current = sum([int(x)**2 for x in str(current)])
            if current == 1:
                return True
        return False

        