class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        ans = []
        for i, num in enumerate(nums):
            if num > target:
                continue
            curr = self.combinationSum(nums[i:], target - num)
            if curr:
                ans += [l + [num] for l in curr]
        return ans