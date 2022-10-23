from math import pow
x,y,M = map(int,input().split())
result = pow(int(x),int(y))%int(M)
print(int(result))