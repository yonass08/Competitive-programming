class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 1
        res = 0

        for i in range(1, len(prices)):
            if prices[i] != prices[i-1] - 1:
                res += (count * (count + 1) ) // 2
                count = 0
            count += 1

        res += (count * (count + 1) ) // 2
        return res
