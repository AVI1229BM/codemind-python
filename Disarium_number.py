from math import pow
n = input()
c = 0
for i in n:
    c += pow(int(i),(n.index(i))+1)
if int(c) == int(n):
    print("True")
else:
    print("False")