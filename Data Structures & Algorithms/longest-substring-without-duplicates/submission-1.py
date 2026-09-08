class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        lp, rp = 0, 1
        chars = set()
        chars.add(s[lp])
        ans = 1
        while rp < len(s):
            while s[rp] in chars:
                chars.remove(s[lp])
                lp += 1
            chars.add(s[rp])
            ans = max(ans, len(chars))
            rp += 1
        return ans