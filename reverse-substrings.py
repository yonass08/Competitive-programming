class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        while '(' in s:
            i = 0
            while i < len(s):
                if s[i] == '(':
                    stack.append(i)
                elif s[i] == ')':
                    match = stack.pop()
                    s = s[:match] + s[i-1:match:-1] + s[i+1:]
                    break
                i += 1
            stack = []
        return s
