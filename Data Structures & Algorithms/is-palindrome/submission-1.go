func isAlphaNum(c byte) bool {
    isAlphaLower := c >= 'a' && c <= 'z'
    isAlphaHigher := c >= 'A' && c <= 'Z'
    isNum := c >= '0' && c <= '9'
    if isAlphaLower || isAlphaHigher || isNum {
        return true
    }
    return false
}

func isPalindrome(s string) bool {
    s = strings.ToLower(s)
    lp, rp := 0, len(s) - 1
    for {
        if lp >= rp {
            break
        }
        if !isAlphaNum(s[lp]) {
            lp++
        } else if !isAlphaNum(s[rp]) {
            rp--
        } else if s[lp] != s[rp] {
            return false
        } else {
            lp++
            rp--
        }
    }
    return true
}
