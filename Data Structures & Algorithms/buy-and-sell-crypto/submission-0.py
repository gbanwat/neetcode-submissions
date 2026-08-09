class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        max_profit=0
        i=0
        j=1
        while i<len(prices)-1 and j<len(prices):
            if prices[j]-prices[i]>0:
                profit=prices[j]-prices[i]
                max_profit=max(profit,max_profit)
                j+=1
            else:
                i=j
                j=i+1
        return max_profit
        