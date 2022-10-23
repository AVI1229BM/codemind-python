n = input()
l = len(n)
e = 0
o = 0
for i in n:
    if int(i)%2==0:
        e+=1
    else:
        o+=1
if e==l:
    print("Even")
elif o==l:
    print("Odd")
else:
    print("Mixed")