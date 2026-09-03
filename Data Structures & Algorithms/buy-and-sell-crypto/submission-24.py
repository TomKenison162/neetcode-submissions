class Solution:
    def maxProfit(self, prices: List[int]) -> int:

       low = prices[0]
       max_profit = 0

       for i in prices[1:]:
            
            if i < low:
                low = i
            max_profit = max(max_profit, i-low)
       return max_profit


                
                


        