class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, ind) for ind, num in enumerate(nums)]
        sorted_arr = sorted(arr)
        # print(sorted_arr)
        l, r = 0, len(nums) - 1
        # assumed that there will always be an ans
        while True:
            actual = sorted_arr[l][0] + sorted_arr[r][0]
            if actual == target:
                break
            if actual < target:
                l += 1
            else:
                r -= 1
        return sorted([sorted_arr[l][1], sorted_arr[r][1]])
