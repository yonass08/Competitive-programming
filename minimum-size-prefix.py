class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[-1] + nums[i])

        res = len(sums)

        for i in range(len(nums)):
            req = sums[i] + target
            if req > sums[-1]: continue

            found = False
            lo, hi = i+1, len(sums)-1
            while lo <= hi:
            
                mid = (lo + hi) // 2
                if sums[mid] < req:
                    lo = mid+1
                elif sums[mid] == req:
                    res = min(res, mid - i)
                    found = True
                    break
                else:
                    hi = mid-1

            if not found:
                res = min(res, lo - i)

        return res % len(sums)
        
    
#30min
