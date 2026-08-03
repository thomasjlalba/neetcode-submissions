class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1
        while lp < rp:
            s = numbers[lp] + numbers[rp]
            if s == target:
                return [lp + 1, rp + 1]
            if s < target:
                lp += 1
            else:
                rp -= 1
        return [-1, -1]