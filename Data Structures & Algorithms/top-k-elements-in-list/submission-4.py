class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap of key = num, val = counts
        numByCounts = {}
        for num in nums:
            if num not in numByCounts:
                numByCounts[num] = 0
            numByCounts[num] += 1
        countsOfNums = {}
        for num, count in numByCounts.items():
            if count not in countsOfNums:
                countsOfNums[count] = []
            countsOfNums[count].append(num)
        sortedCounts = dict(sorted(countsOfNums.items(), reverse=True))
        print(sortedCounts)
        ans = []
        for key, val in sortedCounts.items():
            ans += val
            if len(ans) == k:
                break
        return ans
        
        