class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        num = len(prices)
        profit = 0
        for i in range(num):
            buy = prices[i]
            for j in range(1+i,num):
                sell = prices[j]               
                maxProfit = sell - buy
                profit = max(maxProfit,profit)
        return profit


        