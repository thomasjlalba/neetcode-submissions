func twoSum(numbers []int, target int) []int {
    lp, rp := 0, len(numbers) - 1
    for {
        ans := numbers[lp] + numbers[rp]
        if ans == target {
            break
        }
        if ans < target {
            lp++
        } else {
            rp--
        }
    }
    return []int{lp + 1, rp + 1}
}
