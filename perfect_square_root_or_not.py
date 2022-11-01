n=int(input())
def mani(n):
    for i in range(1,(n+1)//2):
        if i*i==n:
            return True
    return False 
print(mani(n))