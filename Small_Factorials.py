def fact(n):
    pro = 1
    for i in range(1,n+1):
        pro=pro*i
    return pro
t = int(input())
l = []
for i in range(t):
    l.append(int(input()))
for i in range(t):
    print(fact(l[i]))