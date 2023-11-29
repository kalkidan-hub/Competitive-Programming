class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            q, r = n // 3, n % 3
            if r == 2:
                return False
            n = q
        
        return True