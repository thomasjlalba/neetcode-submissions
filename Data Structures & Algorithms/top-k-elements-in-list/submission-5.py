class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        for key, val in counts.items():
            freq[val].append(key)
        ans = []
        for i in range(len(nums), 0, -1):
            ans += freq[i]
            if len(ans) == k:
                return ans