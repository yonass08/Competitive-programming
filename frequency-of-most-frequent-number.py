import math

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        i, sums = 0, 0
        max_count = 0

        for j in range(len(nums)):
            sums += nums[j]
            while sums + k < nums[j] * (j - i + 1):
                sums -= nums[i]
                i += 1
            max_count = max(max_count, j - i + 1)
        
        return max_count
        
                
            
