class Solution:
    def isHappy(self, n: int) -> bool:
        seen_before = set()
        
        while True:
            
            if n in seen_before:
                break
            elif n == 1:
                return True
            
            seen_before.add(n)
            new_n = 0
            for i in str(n):
                new_n += int(i) ** 2
            n = new_n
