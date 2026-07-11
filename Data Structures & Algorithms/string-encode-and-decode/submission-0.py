class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += s
            # indicate end of string
            ans += '\n'
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        curr = ""
        i = 0
        while i < len(s):
            if s[i] == '\n':
                ans.append(curr)
                curr = ""
            else:
                curr += s[i]
            i += 1
        return ans
