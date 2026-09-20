class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # order the piles
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            
            # get the count
            count = 0
            for pile in piles:
                count += math.ceil(pile / mid)
            if count > h:
                l = mid + 1
            else:
                r = mid
        return l