class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for c in range(len(grid)):
            for r in range(len(grid[0])):
                if visited[c][r]:
                    continue
                if grid[c][r] == "0":
                    visited[c][r] = 1
                    continue
                self.dfs(r, c, grid, visited)
                count += 1
        return count
    
    def dfs(self, r, c, grid, visited):
        if r < 0 or r >= len(grid[0]) or c < 0 or c >= len(grid):
            return
        if visited[c][r]:
            return
        visited[c][r] = 1
        if grid[c][r] == "0":
            return
        # island, expand search
        for y, x in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            self.dfs(r + x, c + y, grid, visited)
