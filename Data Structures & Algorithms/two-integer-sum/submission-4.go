func twoSum(nums []int, target int) []int {
    sortedS := make([][2]int, len(nums))
    for i, num := range nums {
        sortedS[i] = [2]int{num, i}
    }

    // sort sortedS
    sort.Slice(sortedS, func(i, j int) bool {
        return sortedS[i][0] < sortedS[j][0] // compare the first indexes
    })

    lp, rp := 0, len(nums) - 1
    for {
        sum := sortedS[lp][0] + sortedS[rp][0]
        if sum == target {
            ans := []int{sortedS[lp][1], sortedS[rp][1]}
            sort.Ints(ans)
            return ans
        } else if sum < target {
            lp++
        } else {
            rp--
        }
    }
}
