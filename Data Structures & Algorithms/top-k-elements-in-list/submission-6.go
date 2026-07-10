func topKFrequent(nums []int, k int) []int {
    hashMap := make(map[int]int)
    for _, num := range nums {
        hashMap[num]++
    }
    count := make([][]int, len(nums) + 1)
    // store all into counts
    for key, val := range hashMap {
        count[val] = append(count[val], key)
    }
    ans := []int{}
    for i := len(nums); i > 0; i-- {
        for _, val := range count[i] {
            ans = append(ans, val)
        }
        if len(ans) == k {
            break
        }
    }
    return ans
}
