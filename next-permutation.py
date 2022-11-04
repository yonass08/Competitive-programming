class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return

        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i+1]: i -= 1

        left, right = 0, 0
        if i == len(nums) - 2:
            left, right = i, i+1

        elif i == -1:
            left, right = 0, len(nums)-1

        else:
            lo = i+1
            hi = len(nums)-1
            mid = 0
            if nums[hi] > nums[i]:
                mid = hi
            else:
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if nums[mid] <= nums[i]:
                        hi = mid-1
                    elif nums[mid+1] > nums[i]:
                        lo = mid+1
                    else:
                        break

            nums[i], nums[mid] = nums[mid], nums[i]
            left, right = i+1, len(nums)-1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return
