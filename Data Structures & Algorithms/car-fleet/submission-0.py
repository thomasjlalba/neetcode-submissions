class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort according to their positions
        l = []
        for i in range(len(position)):
            l.append((position[i], speed[i]))
        l = sorted(l, reverse=True)

        ans = 0
        prevTime = 0

        for (posn, sp) in l:
            # time taken to reach the end
            time = (target - posn) / sp
            if time > prevTime:
                ans += 1
                prevTime = time
        return ans