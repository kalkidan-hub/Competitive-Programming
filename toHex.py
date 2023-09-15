class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        res = ""
        
        if num < 0:
            num += 2 ** 32
        
        after10map = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        
        while num != 0:
            
            r = num % 16
            if r >= 10:
                res += after10map[r]
            else:
                res += str(r)
            
            num //= 16
        
        return res[::-1]
    
    def toHex2(self, num: int) -> str:
        if num == 0:
            return "0"
        
        res = ""

        after10map = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        
        for i in range(8):
            hx = (num >> (4*i)) & 0xf
            
            if hx >= 10:
                res += after10map[hx]
            else:
                res += str(hx)
                
        res = res[::-1]
        
        j = 0
        
        while res[j] == '0':
            j += 1
            
        
        
        return res[j:]

# print(0xff)