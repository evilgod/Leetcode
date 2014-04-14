class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)<2: return 0
        max_profit=0
        min_price=prices[0]
        
        for ix in range(len(prices)):
              
                if prices[ix]<min_price:
                    min_price=prices[ix]
                if prices[ix]-min_price > max_profit:
                    max_profit=prices[ix]-min_price
        return max_profit        
                    