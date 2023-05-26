def reverse(x: int) -> int:
        if x == 0: return x
        sign = x // abs(x)
        x = abs(x)
        res = 0
        
        while x:
            lsd = x % 10 # lowest significant digit
            res *= 10
            res += lsd
            x //= 10
            
        if res < -2**31 or res > 2**31:
            return 0
        return sign * res


def reverse2(x):
    s = str(x)
    if s[0] == '-':
        s = s[0] + s[1:][::-1]
    else:
        s = s[::-1]
    s = int(s)
    if not(s >= 2**31 or s <= -2**31):
        return s
    else:
        return 0