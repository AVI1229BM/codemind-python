def mani(n):
    return str(n)==str(n)[::-1]
n=int(input())
l,f=n-1,n+1
while True:
    if mani(l):
        break
    l-=1
while True:
    if mani(f):
        break
    f+=1
if n-l<f-n:
    print(l)
elif n-l==f-n:
    print(l,f)
else:
    print(f)


