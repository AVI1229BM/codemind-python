t = int(input())
ar = input().split()
s = 0
n = input()
for i in ar:
  if n == i:
    s += int(i)
if s > 0:
    print("True")
else:
    print("False")