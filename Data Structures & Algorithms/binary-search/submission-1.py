class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        lp, rp = 0, len(nums) - 1
        while lp < rp:
            mid = (lp + rp) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lp = mid + 1
            else:
                rp = mid - 1
        if lp == rp and nums[lp] == target:
            return lp
        return -1