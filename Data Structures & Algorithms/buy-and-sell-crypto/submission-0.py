class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maks = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maks = max(maks, prices[j] - prices[i])
        return maks

