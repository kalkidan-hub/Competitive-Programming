def countBits(n):
    # brute force
    def ones(n):
        one = 0
        while n:
            one += n&1
            n//= 2
        return one
    ans = []
    for i in range(n+1):
        ans.append(ones(i))
    
    return ans 

def countBits2(n):
    ans = []
    for i in range(n + 1):
        ones = 0
        while i != 0:
            ones += i&1
            i >>= 1
        ans.append(ones)
    return ans


res = countBits2(20)
print(res)

