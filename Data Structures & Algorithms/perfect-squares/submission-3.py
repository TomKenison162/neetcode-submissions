
class Solution:
    def numSquares(self, n: int) -> int:

        cache = [float("inf")] *(n +1)
        cache[0] =0
     
        for i in range(1, n+1):
            for j in range(1, int((i) ** 0.5 ) +1):
                cache[i] =  min(cache[i], cache[i - (j **2)] +1)

        print(cache)
        return cache[-1]
        