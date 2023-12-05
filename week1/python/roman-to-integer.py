class Solution:
    def romanToInt(self, s: str) -> int:
        _map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        prev = ""
        for n in s:
            condition = ((n == 'V' or n == 'X') and prev == 'I') or ((n == 'L' or n == 'C') and prev == 'X') or ((n == 'D' or n == 'M') and prev == 'C')
            if condition:
                num += (_map[n] - 2*_map[prev])
            else:
                num += _map[n]
            prev = n
        
        return num