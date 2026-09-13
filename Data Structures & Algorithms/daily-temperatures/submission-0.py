class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        idx = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            # check the stack and see if temp > stack
            while len(stack) > 0 and stack[-1] < temp:
                ans[idx[-1]] = i - idx[-1]
                stack.pop()
                idx.pop()
            stack.append(temp)
            idx.append(i)
        return ans
