import bisect
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # bintree
        stones = sorted(stones)
        while len(stones) > 1:
            # remove top 2 stones and get remainder
            rem = stones.pop() - stones.pop()
            if rem == 0:
                continue
            # insert to correct spot
            idx = bisect.bisect_left(stones, rem)
            stones.insert(idx, rem)
        if len(stones) == 0:
            return 0
        return stones[0]
