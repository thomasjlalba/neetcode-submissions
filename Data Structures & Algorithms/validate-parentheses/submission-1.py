class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        order = []
        for c in s:
            if c in brackets.values():
                # add to order
                order.append(c)
            else:
                if len(order) == 0 or brackets[c] != order[-1]:
                    return False
                order.pop()
        if len(order) != 0:
            return False
        return True