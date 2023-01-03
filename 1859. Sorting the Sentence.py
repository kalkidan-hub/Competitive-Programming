class Solution:
    def sortSentence(self, s: str) -> str:
        word=list(s.split())
        lst=[]
        corrSent=""
        for i in word:
            lst+=[int(i[-1])]
        for i in range(len(word)):
            for j in lst:
                if i==j-1:
                    corrSent+=word[lst.index(j)][:-1]+" "
        return corrSent[:-1]