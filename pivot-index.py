class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        totalSum = 0
        
        for i in nums:
            totalSum += i
        
        i = 0
        while i < len(nums):
            rightSum = totalSum - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            i += 1
        return -1
