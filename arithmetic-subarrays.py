class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            subarray = nums[l[i]: r[i]+1]
            if len(subarray) < 2:
                result.append(False)
                continue
            subarray.sort()
            
            diff = subarray[1] - subarray[0]
            for j in range(2, len(subarray)):
                if subarray[j] - subarray[j-1] != diff:
                    result.append(False)
                    break
            
            if len(result) < i+1:
                result.append(True)
        
        return result
                
