class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSet = {nums[0]: 0}
        for i in range(1, len(nums)):
            for num, ind in numsSet.items():
                if nums[i] + num == target:
                    return [ind, i]
            numsSet[nums[i]] = i