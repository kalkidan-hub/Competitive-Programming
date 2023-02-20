class Solution:
    def isHappy(self, n: int,notHappy) -> bool:
        notHappy += [n]
        if notHappy[-1] == 1:
            return True
        squareSum = 0
        th = 10
        ct = 1
        while n != 0:
            squareSum += (n % (th/ct) ) ** 2
            n //= th
            ct = th
            th *= 10
        if squareSum in notHappy:
            return False
        notHappy += [squareSum]
        return self.isHappy(squareSum, notHappy)
    def isHappy2(self,n):
        notHappy = [n]
        while notHappy[-1] != 1:
            squareSum = 0
            th = 10
            ct = 1
            while n != 0:
                squareSum += (n % (th/ct) ) ** 2
                n //= 10
                ct = th
                th *= 10
            if squareSum in notHappy:
                return False
            notHappy += [squareSum]
            print(notHappy)
            n = squareSum
        return True
def func(n):
    squareSum = 0
    th = 10
    ct = 1
    while n != 0:
        squareSum += (n % (th/ct) ) ** 2
        n //= 10
        ct = th
        th *= 10
    return squareSum
    
