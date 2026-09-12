func characterReplacement(s string, k int) int {
	count := make(map[byte]int)
    l, maxFreq, ans := 0, 0, 0
    for r := 0; r < len(s); r++ {
        count[s[r]]++
        maxFreq = max(maxFreq, count[s[r]])
        for r - l + 1 - maxFreq > k {
            count[s[l]]--
            l++
        }
        ans = max(r - l + 1, ans)
    }
    return ans
}
