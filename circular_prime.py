def mani(i):
    if i==2:
        return (True)
    for j in range(2,(n+1)//2):
        if i%j==0:
            return(False)
    return(True)
n=int(input())
if mani(n) and mani(int(str(n)[::-1])):
    print("circular prime")
elif mani(n):
    print('prime but not a circular prime')
else:
    print('not prime')
