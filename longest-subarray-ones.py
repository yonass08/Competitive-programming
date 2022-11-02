class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] == 0: zeros += 1
                
            if zeros > 1:
                if nums[slow] == 0: zeros -= 1
                slow += 1
                
        return fast - slow
