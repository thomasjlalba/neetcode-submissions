class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        ans = 0
        l, r, maxfreq = 0, 0, 0
        while r < len(s):
            if s[r] not in hm:
                hm[s[r]] = 0
            hm[s[r]] += 1
            # update the max occuring character count
            maxfreq = max(maxfreq, hm[s[r]])

            while (r - l + 1) - maxfreq > k:
                hm[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans