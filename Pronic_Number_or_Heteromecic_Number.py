n = int(input())
c = 0
for i in range(1,int(n/2)+1):
    if i*(i+1) == n:
        c+=1
    else:
        c-+1
if c>0:
    print("YES")
else:
    print("NO")