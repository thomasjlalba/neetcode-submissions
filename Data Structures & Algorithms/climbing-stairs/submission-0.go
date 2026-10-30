func climbStairs(n int) int {
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
    step := make([]int, n)
	step[0] = 1
	step[1] = 2
	for i := 2; i < n; i++ {
		step[i] = step[i - 1] + step[i - 2]
	}
	return step[n - 1]
}
