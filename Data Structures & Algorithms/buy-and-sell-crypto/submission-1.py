class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        c_profit = 0
        i=0
        while i<n-1:
            r = i + 1
            while r<n and prices[r] > prices[i]:
                temp = prices[r]-prices[i]
                if temp > c_profit:
                    c_profit = temp
                r+=1
            i = r
        return c_profit