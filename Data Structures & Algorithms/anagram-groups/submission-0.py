class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedMap = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS not in sortedMap:
                sortedMap[sortedS] = []
            sortedMap[sortedS].append(s)
        return [l for l in sortedMap.values()]