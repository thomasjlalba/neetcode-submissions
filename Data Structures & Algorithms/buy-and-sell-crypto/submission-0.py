class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp = 0, 1
        maxP = 0
        while rp < len(prices):
            curr = prices[rp] - prices[lp]
            if curr > 0:
                maxP = max(maxP, curr)
            else:
                lp = rp
            rp += 1
        return maxP