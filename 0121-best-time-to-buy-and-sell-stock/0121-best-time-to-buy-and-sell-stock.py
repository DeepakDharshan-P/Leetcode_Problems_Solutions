class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        p = 0
        m = p
        for curr in range(1,len(prices)):
            if buy > prices[curr]:
                buy = prices[curr]
            if prices[curr] > buy:
                p = prices[curr] - buy
                m = max(p,m)
        return m