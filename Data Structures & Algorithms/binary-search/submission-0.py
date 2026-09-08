import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind = bisect.bisect_left(nums, target)
        if ind == len(nums) or nums[ind] != target:
            return -1
        return ind