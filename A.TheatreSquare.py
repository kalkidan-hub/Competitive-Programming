def flagSquare(n,m,s):
    if n%s!=0:
        l=n//s + 1 
    else:
        l=n//s
    ct=1
    while m>s:
        m=m-s
        ct+=1
    return l*ct

n,m,s=map(int,input().split())
if n%s!=0:
        l=n//s + 1 
else:
    l=n//s
ct=1
while m>s:
    m=m-s
    ct+=1
print(l*ct)
