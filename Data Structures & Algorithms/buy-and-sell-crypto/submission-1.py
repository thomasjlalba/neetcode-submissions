class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 101
        maxP = 0
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                maxP = max(maxP, price - lowest)
        return maxP