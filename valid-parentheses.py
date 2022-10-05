class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = '({['
        closing = ")}]"
        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing:
                if len(stack) == 0:
                    return False
                if opening.index(stack.pop()) != closing.index(i):
                    return False
            
        return len(stack) == 0
