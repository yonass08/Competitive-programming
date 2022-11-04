class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        left = 0

        while left < len(arr)-1:
            right = left + 1
            if arr[right] > arr[left]:
                while right+1 < len(arr) and arr[right+1] > arr[right]:
                    right += 1

                if right+1 < len(arr) and arr[right+1] < arr[right]:
                    while right+1 < len(arr) and arr[right+1] < arr[right]:
                        right += 1

                    res = max(res, right-left+1)

            left = right

        return res

        
