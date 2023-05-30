class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        shift = len(num1)-1
        ans = 0
        for i in num1:
            mul = int(i) * int(num2)
            ans += mul*(10**shift)
            shift -=1
        return str(ans)