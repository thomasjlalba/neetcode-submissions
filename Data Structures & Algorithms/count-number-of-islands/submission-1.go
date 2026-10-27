func numIslands(grid [][]byte) int {
    visited := make([][]bool, len(grid))
	for i := range len(grid) {
		visited[i] = make([]bool, len(grid[0]))
	}
	count := 0
	for r := range len(grid) {
		for c := range len(grid[0]) {
			if visited[r][c] {
				continue
			}
			if grid[r][c] == '0' {
				visited[r][c] = true
				continue
			}
			dfs(r, c, visited, grid)
			count++
		}
	}
	return count
}

func dfs(r int, c int, visited [][]bool, grid [][]byte) {
	if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[0]) || visited[r][c] {
		return
	}
	visited[r][c] = true
	if grid[r][c] == '0' {
		return
	}
	for _, d := range []struct{ x, y int }{{-1, 0}, {1, 0}, {0, -1}, {0, 1}} {
		dfs(r + d.x, c + d.y, visited, grid)
	}
}