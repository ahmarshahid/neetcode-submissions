class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num = len(prices)
        profit = 0
        for i in range(num):
            for j in range(1+i,num):
                profit = max(prices[j]-prices[i],profit)
        return profit


        