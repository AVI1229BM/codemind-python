t = int(input())
ar = input().split()
s = 0
for i in ar:
    if int(i)%2 != 0:
        s += int(i)
print(s)