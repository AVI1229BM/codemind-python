n,x=map(int,input().split())
d=10**x
l=n%d
f=int(str(n)[:x])
if l>f:
    print(l-f)
else:
    print(f-l)