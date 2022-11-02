def mani(n):
    for i in range(2,(n-2)//2):
        if n%i==0:
            return("not a prime")
    return("prime")
n=int(input())
print(mani(n))