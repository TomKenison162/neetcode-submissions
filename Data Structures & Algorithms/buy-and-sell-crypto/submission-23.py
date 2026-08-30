class Solution:
    def maxProfit(self, prices: List[int]) -> int:

      
        low = prices[0]
        max_profit = 0
        buy, sell = 0,1
        for i in range(1, len(prices)):
            
            if prices[i] < prices[buy]:
                buy = i
                low = prices[i]
            sell = i 
            
            
                
            print(buy, sell, max_profit)
            max_profit = max(max_profit, prices[sell]-prices[buy] )
        return max_profit


                
                


        