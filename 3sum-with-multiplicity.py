class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = 0
        arr.sort()
        
        for i in range(len(arr)-2):
            summ = target - arr[i]
            left = i + 1
            right = len(arr)-1
            
            while left < right:
                if arr[left] + arr[right] < summ:
                    left += 1
                elif arr[left] + arr[right] > summ:
                    right -= 1
                elif arr[left] == arr[right]:
                    count += (right - left + 1) * (right - left) // 2
                    count %= 1000000007
                    break
                else:
                    temp1, temp2 = 0, 0
                    lnum, rnum = arr[left], arr[right]
                    
                    while arr[left] == lnum:
                        temp1 += 1
                        left += 1
                    
                    while arr[right] == rnum:
                        temp2 += 1
                        right -= 1
                        
                    count += temp1 * temp2
                    count %= 1000000007
                
                    
        return count
                    
                    
