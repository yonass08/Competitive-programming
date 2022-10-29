import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        class string:
            def __init__(self, word):
                self.word = word
                
            def __lt__(self, other):
                return self.word > other.word
            
        hashmap = {}
        for word in words:
            hashmap[word] = hashmap.get(word, 0) + 1
            
        items = [(count, string(word)) for word, count in hashmap.items()]
        heap = []
        
        for item in items:
            heapq.heappush(heap, item)
            if len(heap) > k:
                heapq.heappop(heap)
                
        res = [None] * len(heap)
        i = len(heap)-1
        while heap:
            res[i] = heapq.heappop(heap)[1].word
            i -= 1
               
        return res
