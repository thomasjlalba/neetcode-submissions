func evalRPN(tokens []string) int {
    stack := make([]int, 0)
    for _, token := range tokens {
        num, err := strconv.Atoi(token)
        if err == nil {
            // actual number
            stack = append(stack, num)
            continue
        }
        // operator
        num1 := stack[len(stack) - 2]
        num2 := stack[len(stack) - 1]
        switch token {
        case "+":
            num = num1 + num2
        case "-":
            num = num1 - num2
        case "*":
            num = num1 * num2
        case "/":
            num = num1 / num2
        }
        stack = append(stack[:len(stack) - 2], num)
    }
    return stack[0]
}
