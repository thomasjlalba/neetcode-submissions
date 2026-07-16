func longestConsecutive(nums []int) int {
    mp := make(map[int]int)
    ans := 0
    for _, num := range nums {
        if mp[num] > 0 {
            continue
        }
        left := mp[num - 1]
        right := mp[num + 1]
        mp[num] = left + right + 1
        ans = max(ans, mp[num])
        mp[num - left] = mp[num]
        mp[num + right] = mp[num]
    }
    return ans
}
