n=int(input())
n1,n2=0,1
N=[]
while True:
    n3=n2+n1
    n1=n2
    n2=n3
    N.append(n2)
    if n2>n:
        break
x=abs(n-N[-1])
y=abs(n-N[-2])
if x==y:
    print(N[-2],N[-1])
else:
    Min=min(x,y)
    if Min==x:
        print(N[-1])
    else:
        print(N[-2])