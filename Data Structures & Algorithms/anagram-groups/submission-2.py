class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            # bucket sort O(n)
            countS = [0] * 26
            for c in s:
                countS[ord(c) - ord('a')] += 1
            sortedS = tuple(countS)
            if sortedS not in hashMap:
                hashMap[sortedS] = []
            hashMap[sortedS].append(s)
        return [l for l in hashMap.values()]