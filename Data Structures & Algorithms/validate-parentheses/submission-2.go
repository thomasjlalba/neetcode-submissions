func isValid(s string) bool {
    brackets := make(map[rune]rune)
    brackets[')'] = '('
    brackets[']'] = '['
    brackets['}'] = '{'
    open := make(map[rune]struct{})
    open['('] = struct{}{}
    open['['] = struct{}{}
    open['{'] = struct{}{}
    var stack []rune

    for _, c := range s {
        if _, exists := open[c]; exists {
            stack = append(stack, c)
        } else {
            if len(stack) == 0 || stack[len(stack) - 1] != brackets[c] {
                return false
            }
            stack = stack[:len(stack) - 1]
        }
    }
    if len(stack) != 0 {
        return false
    }
    return true
}
