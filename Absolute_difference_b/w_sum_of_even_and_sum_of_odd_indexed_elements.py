n = int(input())
ar = input().split()
e = 0
o = 0
for i in range(0,n):
    if i%2 == 0:
        e += int(ar[i])
    else:
        o += int(ar[i])
if e - o <0:
    print(-(e-o))
else:
    print(e-o)