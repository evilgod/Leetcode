class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        
        profit =0
        for ix in range(len(prices)):
            if ix+1 < len(prices) and prices[ix+1]-prices[ix]>0:
                profit = profit+ prices[ix+1]-prices[ix]
                
        return profit 