class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            if x == 0:
                return None
            return 1 / self.myPow(x, 0-n)
        if n == 0:
            return 1
        temp = x
        answer = 1
        
        quotient, remainder = n, 0
        while quotient > 0:
            remainder = quotient % 2
            quotient = quotient // 2
            if remainder == 1:
                answer *= temp
            temp = temp * temp
            
            
        return answer
