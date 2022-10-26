t = int(input())
ar = input().split()
s = 0
n = 0
for i in ar:
    s += int(i)
for i in ar:
    if str(int(s/(len(ar)))) == i:
        n += 1
if n>0:
    print("True")
else:
    print("False")