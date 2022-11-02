class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        windowSum = 0
        
        for i in range(len(arr)):
            if i >= k-1:
                windowSum += arr[i]
                if windowSum / k >= threshold: res += 1
                windowSum -= arr[i-k+1]
            else:
                windowSum += arr[i]
                
        return res
