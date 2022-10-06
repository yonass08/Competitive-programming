class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        slow,fast = 0,0
        while fast < len(nums):
            if nums[slow] != 0:
                slow += 1
                fast += 1
            else:
                while fast < len(nums) and nums[fast] ==  0:
                    fast += 1
                if fast == len(nums):
                    return
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return
                
