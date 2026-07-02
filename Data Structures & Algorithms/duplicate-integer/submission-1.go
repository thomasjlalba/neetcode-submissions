func hasDuplicate(nums []int) bool {
    set := make(map[int]struct{})
    for _, num := range nums {
        _, isExist := set[num]
        if isExist {
            return true
        }
        set[num] = struct{}{}
    }
    return false
}
