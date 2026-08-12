class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = 1e9
        maksP = 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res





