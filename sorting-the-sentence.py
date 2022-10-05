class Solution:
    def sortSentence(self, s: str) -> str:
        list = s.split(' ')
        for i in range(len(list)-1):
            for j in range(len(list)-i-1):
                if(int(list[j][-1]) > int(list[j+1][-1])):
                    list[j], list[j+1] = [list[j+1], list[j]]
        
        for i in range(len(list)):
            list[i] = list[i][:-1]
        return " ".join(list)
