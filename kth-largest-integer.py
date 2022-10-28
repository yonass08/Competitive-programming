import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap = []
        
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(heap, int(nums[i]))
            elif int(nums[i]) > heap[0]:
                heapq.heapreplace(heap, int(nums[i]))
            
        return str(heap[0])
