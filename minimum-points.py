class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = 0
        for i in range(k):
            window += cardPoints[i]
         
        maxSum = window
        for i in range(k):
            window = window - cardPoints[k-i-1] + cardPoints[-i-1]
            maxSum = max(window, maxSum)
                         
        return maxSum
