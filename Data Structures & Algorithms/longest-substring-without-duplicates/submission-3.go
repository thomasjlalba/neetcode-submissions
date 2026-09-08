func lengthOfLongestSubstring(s string) int {
    if len(s) == 0 {
        return 0
    }
    lp, rp := 0, 1
    chars := make(map[byte]struct{})
    chars[s[lp]] = struct{}{}
    ans := 1
    for ;rp < len(s); rp++ {
        for _, exists := chars[s[rp]]; exists; lp++ {
            delete(chars, s[lp])
            _, exists = chars[s[rp]]
        }
        chars[s[rp]] = struct{}{}
        ans = max(ans, len(chars))
    }
    return ans
}
