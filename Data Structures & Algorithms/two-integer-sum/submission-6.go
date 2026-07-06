func twoSum(nums []int, target int) []int {
    numsMap := map[int]int{}
    for i, num := range nums {
        other := target - num
        val, ok := numsMap[other]
        if ok {
            return []int{val, i}
        }
        numsMap[num] = i
    }
    return []int{-1, -1}
}
