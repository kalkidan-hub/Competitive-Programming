class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        flag = False
        q = num
        if num < 0:
            flag = True
            q = -num
        
        res = ""
        
        while q != 0:
            res += str(q % 7)
            q = q // 7
        
        res = res[::-1]
        return "-" + res if flag else res