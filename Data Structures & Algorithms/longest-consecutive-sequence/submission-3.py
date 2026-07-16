class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in hashset:
                curr = 0
                val = num
                while val in hashset:
                    curr += 1
                    val += 1
                longest = max(longest, curr)
        return longest