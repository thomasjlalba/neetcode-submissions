import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse=True)
        if len(self.nums) < k:
            self.nums += [-1001] * (k - len(self.nums))
        else:
            self.nums = self.nums[:k]

    def add(self, val: int) -> int:
        idx = bisect.bisect_right(self.nums, -val, key=lambda x: -x)
        
        # insert in index
        self.nums.insert(idx, val)
        # remove last one
        self.nums.pop()
        print(self.nums)
        return self.nums[-1]

