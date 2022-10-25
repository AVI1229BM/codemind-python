n = int(input())
ar = input().split()
o = 0
for i in range(0,n):
    if i%2==0:
        o += int(ar[i])
print(o)
    