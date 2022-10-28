class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while len(stack) > 0 and digit < stack[-1] and k > 0:
                stack.pop()
                k -= 1     
            stack.append(digit)
          
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
            
        result = "".join(stack[i: len(stack)-k])
        return "0" if result == '' else result
                
