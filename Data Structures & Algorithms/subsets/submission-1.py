class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            new_ans = []
            for l in ans:
                new_ans.append(l + [num])
            ans += new_ans
        return ans