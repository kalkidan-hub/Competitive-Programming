class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqr_root = c**(0.5)
        
        i, j = 0,int(sqr_root) + 1

        while i <= j:
            if i**2 + j**2 > c:
                j -= 1
            elif i**2 + j**2 < c:
                i += 1
            else:
                return True
        return False
                