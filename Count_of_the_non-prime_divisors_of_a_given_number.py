def isprime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
n = int(input())
count = 0
for i in range(1,n+1):
    if n%i==0 and isprime(i)==False:
        count+=1
print(count)