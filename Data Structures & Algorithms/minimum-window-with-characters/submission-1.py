class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # get map of t
        tMap = {}
        cnts = {}
        for c in t:
            if c not in tMap:
                tMap[c] = 0
                cnts[c] = 0
            tMap[c] += 1
        
        ans = ""
        l = 0
        for r in range(len(s)):
            if s[r] not in tMap:
                continue
            cnts[s[r]] += 1

            # check if window is good
            done = True
            for k, v in tMap.items():
                if cnts[k] < v:
                    done = False
                    break
            if not done:
                continue
            
            # window is good, l++ until shortest window for given r
            while l <= r:
                if ans == "" or len(ans) > r - l + 1:
                    ans = s[l:r + 1]
                # remove l and increment
                if s[l] in tMap:
                    cnts[s[l]] -= 1
                    if cnts[s[l]] < tMap[s[l]]:
                        l += 1
                        break
                l += 1


        return ans
            