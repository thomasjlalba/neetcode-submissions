class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in numsMap:
                return [numsMap[other], i]
            numsMap[num] = i
        return [-1, -1]
