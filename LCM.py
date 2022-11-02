n,m=map(int,input().split())
y=max(n,m)
x=min(n,m)
m=y
while True:
    if y%x==0:
        break
    y+=m
print(y)
    
