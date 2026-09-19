class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack  and temperatures[i] > stack[-1][0]:
                curr, inx = stack.pop()
                res[inx] = (i - inx)
            stack.append((temperatures[i], i))
        return res
            

        
        