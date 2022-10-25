n = int(input())
ar = input().split()
e = 0
o = 0
for i in ar:
    if int(i)%2 == 0:
        e += int(i) 
    else:
        o += int(i)
if e - o <0:
    print(-(e-o))
else:
    print(e-o)