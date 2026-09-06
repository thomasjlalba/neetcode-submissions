class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                # take the last 2 numbers
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    ans = num1 + num2
                elif token == "-":
                    ans = num1 - num2
                elif token == "*":
                    ans = num1 * num2
                else:
                    ans = int(num1 / num2)
                stack.append(ans)
            else:
                # add number in
                stack.append(int(token))
            # print(stack)
        return stack[0]