class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        ans = set()
        for i in range(len(snums) - 2):
            j, k = i + 1, len(snums) - 1
            while j < k:
                check = snums[i] + snums[j] + snums[k]
                if check == 0:
                    ans.add(tuple([snums[i], snums[j], snums[k]]))
                    j += 1
                    k -= 1
                elif check < 0:
                    j += 1
                else:
                    k -= 1
        return [list(t) for t in ans]