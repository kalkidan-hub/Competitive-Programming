class Solution:
    def countGoodNumbers(self, n: int) -> int:

        # even_spot = math.ceil(n/2)
        
        mod = (10 ** 9 + 7)
        odd_spot = n//2
        even_spot = n - odd_spot
        
        def recursion_pow(base, exp):
            if exp == 0:
                return 1
             
            tmp = recursion_pow(base,exp//2)
            
            if (exp) % 2 == 1:
                return (tmp * tmp * base) % mod
            else:
                return (tmp * tmp) % mod
        
        # print(recursion_pow(2,10))
            
        
        return (recursion_pow(4,odd_spot) * recursion_pow(5,even_spot)) % mod