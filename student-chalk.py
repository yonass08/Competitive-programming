class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if k < chalk[0]: return 0
        
        for i in range(1, len(chalk)):
            chalk[i] += chalk[i-1]
            if k < chalk[i]: return i

        k %=  chalk[-1]

        left, right = 0, len(chalk)-1
        while left <= right:
            mid = (left + right) // 2
            if chalk[mid] < k:
                left = mid + 1
            elif chalk[mid] == k:
                return mid + 1
            else:
                right = mid - 1

        return left
