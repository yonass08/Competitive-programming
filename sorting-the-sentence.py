class Solution:
    def sortSentence(self, s: str) -> str:
        s_split = s.split(' ')
        count = len(s_split)
        result = [''] * count
        
        for i in range(count):
            result[int(s_split[i][-1]) - 1] = s_split[i][:-1]

        return " ".join(result)
