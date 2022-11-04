class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = 0
        mod = 1000000007
        nums = [0] * 101

        for num in arr:
            nums[num] += 1

        for i in range(101):
            summ = target - i
            left = i 
            right = 100
            
            while left <= right:
                if nums[left] == 0: 
                    left += 1
                elif nums[right] == 0:
                    right -= 1
                elif left + right > summ:
                    right -= 1
                elif left + right < summ:
                    left += 1
                elif i < left and left < right:
                    count += nums[i] * nums[left] * nums[right]
                    count %= mod
                    left += 1
                    right -= 1
                elif i < left and left == right:
                    count += (nums[i] * nums[left] * (nums[left]-1)) // 2
                    count %= mod
                    break
                elif i == left and left < right:
                    count += (nums[i] * (nums[i]-1) * nums[right]) // 2
                    count %= mod
                    left += 1
                    right -= 1
                else:
                    count += (nums[i] * (nums[i]-1) * (nums[i]-2)) // 6
                    count %= mod
                    break
                              
        return count
                    
                    
