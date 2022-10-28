import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            
        items = [(count, num) for num, count in hashmap.items()]
        heap = []
        
        for item in items:
            heapq.heappush(heap, item)
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [item[1] for item in heap]
