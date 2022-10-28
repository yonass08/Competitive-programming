class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dictionary = {}
        for num in arr:
            dictionary[num] = dictionary.get(num, 0) + 1
            
        freq = sorted(dictionary.values())
        sum = 0

        for i in range(len(freq)-1, -1, -1):
            sum += freq[i]
            if sum * 2 >= len(arr):
                return len(freq) - i
            
        return len(freq)
