class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            # append length and \n
            ans += chr(len(s))
            ans += "\n"
            ans += s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            # get the length and slice
            size = ord(s[i])
            ans.append(s[i + 2:i + 2 + size])
            i += 2 + size
        return ans
