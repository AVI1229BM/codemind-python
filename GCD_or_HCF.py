n,m=map(int,input().split())
l=min(n,m)
for i in range(l,0,-1):
    if m%i==0 and n%i==0:
        print(i)
        break