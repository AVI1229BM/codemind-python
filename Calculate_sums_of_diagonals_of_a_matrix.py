n=int(input())
a=[]
psum,ssum=0,0
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if i==j:
           psum+=a[i][j]
        if n-1-i==j:
            ssum+=a[i][j]
print('Principal Diagonal:',psum,sep="")
print('Secondary Diagonal:',ssum,sep="")