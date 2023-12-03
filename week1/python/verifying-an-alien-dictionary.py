class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        _order = {ord:i for i,ord in enumerate(order)}

        def check(w1,w2,_order):
            if w1 == w2:
                return True
            i,j = 0,0
            while i < len(w1) and j < len(w2) and w1[i] == w2[j]:
                i += 1
                j += 1
            if j >= len(w2):
                return False
            if i >= len(w1):
                return True
            return _order[w1[i]] < _order[w2[j]]

        for i in range(1,len(words)):
            if not check(words[i-1],words[i],_order):
                return False
        
        return True



        