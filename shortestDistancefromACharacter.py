from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        j_list = [float("inf")]
        
        for i in range(len(s)):
            if s[i] == c:
                j_list.append(i)
        
        j_list.append(float("inf"))
        j = 0
        res = []
        
        
        print(j_list)
        for i in range(len(s)):
            if s[i] == c:
                j += 1
            
            res.append(min(abs(j_list[j] - i), abs(j_list[j + 1] - i)))
        
        return res