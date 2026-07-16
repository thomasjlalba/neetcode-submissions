func longestConsecutive(nums []int) int {
    set := make(map[int]struct{})
    for _, num := range nums {
        set[num] = struct{}{}
    }
    
    ans := 0

    for key := range set {
        _, found := set[key - 1]
        if !found {
            curr := 1
            for {
                if _, exists := set[key + curr]; exists {
                    curr++
                } else {
                    break
                }
            }
            ans = max(curr, ans)
        }
    }
    return ans
}
