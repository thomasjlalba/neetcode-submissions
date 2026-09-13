func dailyTemperatures(temperatures []int) []int {
    ans := make([]int, len(temperatures))
    stack := make([]int, 0)

    for i, temp := range temperatures {
        for len(stack) > 0 {
            last_idx := stack[len(stack) - 1]
            if temperatures[last_idx] < temp {
                ans[last_idx] = i - last_idx
                stack = stack[:len(stack) - 1]
            } else {
                break
            }
        }
        stack = append(stack, i)
    }
    return ans
}
