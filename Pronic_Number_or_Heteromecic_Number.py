n = int(input())
c = 0
for i in range(0,int(n/2)+1):
   if i*(i+1) == n:
       c += i
if c*(c+1) == n:
    print("YES")
else:
    print("NO")
     