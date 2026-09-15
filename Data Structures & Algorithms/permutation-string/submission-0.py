class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # get a hm of the chars in s1
        hm = {}
        for c in s1:
            if c not in hm:
                hm[c] = 0
            hm[c] += 1
        
        # sliding window
        l = 0
        for r in range(len(s2)):
            print(r)
            while s2[r] not in hm and l < r:
                if s2[l] not in hm:
                    hm[s2[l]] = 0
                hm[s2[l]] += 1
                l += 1
            if s2[r] in hm:
                hm[s2[r]] -= 1
                if hm[s2[r]] == 0:
                    hm.pop(s2[r])
            else:
                l += 1
            if len(hm) == 0:
                return True
        return False