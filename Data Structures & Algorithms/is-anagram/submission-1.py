class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            # for s
            if s[i] not in s_map:
                s_map[s[i]] = 0
            s_map[s[i]] += 1

            # for t
            if t[i] not in t_map:
                t_map[t[i]] = 0
            t_map[t[i]] += 1
        
        # compare s_map and t_map
        return s_map == t_map