
class Solution:
    def climbStairs(self, n: int) -> int:
        stair = [-1]* n

        def dyn(i):

            if i >= n:
                return i == n
            if stair[i] != -1:
                return stair[i]
            stair[i] = dyn(i+1) + dyn(i+2)
            

            return dyn(i+1) + dyn(i+2)
        return dyn(0)
        