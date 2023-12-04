class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n,m = len(num1), len(num2)
        n1, n2 = 0, 0

        for i in range(n):
            n1 += int(num1[i])*10**(n-i-1)
        
        for j in range(m):
            n2 += int(num2[j]) * 10**(m-j-1)

        return str(n1 * n2)