class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue
                ans = max(self.dfs(r, c, grid), ans)
        return ans
    def dfs(self, r, c, grid):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0
        
        ans = 1
        grid[r][c] = 0 # to ensure it is not rechecked
        for y, x in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ans += self.dfs(r + y, c + x, grid)

        return ans