class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums), 2):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            if i < len(nums) - 1 and nums[i+1] > nums[i]:
                nums[i+1], nums[i] = nums[i], nums[i+1]
        
        return nums
