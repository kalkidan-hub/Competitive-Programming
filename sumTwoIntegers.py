class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        # that works only for positive integers...
        carry = 0
        res, ct = 0, 0        
        
        while a != 0 or b != 0:
            
            
            mini_sum = carry ^ ((a & 1) ^ (b & 1))
            
            carry = (a & 1) & (b & 1) | (carry & (a & 1)) | (carry & (b & 1))
            
            a >>= 1
            b >>= 1
            
            # updating res, 
            
            # res += mini_sum * (2 ** ct) ## the obsolete 
            res |= mini_sum << ct
            
            ct += 1
            
        return res | (carry << ct)
    
    def getSum_thatIdidntGet(self, a:int, b:int):
        
        mask = 0xFFFFFFFF  # 32-bit mask for two's complement representation
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)