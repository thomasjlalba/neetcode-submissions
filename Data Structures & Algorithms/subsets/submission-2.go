func subsets(nums []int) [][]int {
	ans := make([][]int, 0)
	emp := make([]int, 0)
	ans = append(ans, emp)
	for _, num := range nums {
		sub := make([][]int, 0)
		for _, l := range ans {
			tmp := make([]int, len(l))
			copy(tmp, l)
			tmp = append(tmp, num)
			sub = append(sub, tmp)
		}
		ans = append(ans, sub...)
	}
	return ans
}
