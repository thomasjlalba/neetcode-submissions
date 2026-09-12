class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp, rp = 0, len(heights) - 1
        ans = 0
        while lp < rp:
            ans = max(ans, min(heights[lp], heights[rp]) * (rp - lp))
            # keep the tallest, move the shortest
            if heights[lp] > heights[rp]:
                rp -= 1
            else:
                lp += 1
        return ans