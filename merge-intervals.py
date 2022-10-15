class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.quick_sort(intervals)
        result = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(result[-1][1], intervals[i][1])
                
        return result
        
    def quick_sort(self, intervals, start = 0, end = None):
        if end == None:
            end = len(intervals) - 1
            
        if end > start:
            pivot = self.partition(intervals, start, end)
            self.quick_sort(intervals, start, pivot - 1)
            self.quick_sort(intervals, pivot + 1, end)
        
    def partition(self, intervals, start, end):
        pivot_val = intervals[end][0]
        i = start - 1
        
        for j in range(start, end):
            if intervals[j][0] <= pivot_val:
                i += 1
                intervals[i], intervals[j] = intervals[j], intervals[i]
        
        intervals[i + 1], intervals[end] = intervals[end], intervals[i + 1]
        return i + 1
