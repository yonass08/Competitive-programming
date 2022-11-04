class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sums = []
        currSum = 0
        for i in range(n):
            if i >= k-1:
                currSum += nums[i]
                sums.append(currSum)
                currSum -= nums[i-k+1]
            else:
                currSum += nums[i]

        m = len(sums)
        left = [0] * m
        right = [0] * m

        best = 0
        for i in range(m):
            if sums[i] > sums[best]: best = i
            left[i] = best

        best = m - 1
        for i in range(m-1, -1, -1):
            if sums[i] >= sums[best]: best = i
            right[i] = best

        res = None
        for i in range(k, m-k):
            l, r = left[i-k], right[i+k]
            if res == None or \
            (sums[l] + sums[i] + sums[r]) > (sums[res[0]] + sums[res[1]] + sums[res[2]]):
                res = [l, i, r]
                

        return res

