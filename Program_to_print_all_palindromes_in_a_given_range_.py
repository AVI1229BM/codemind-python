def ispalinedrome(n):
    if str(n)[::-1]==str(n):
       return True
    return False
m=int(input());n = int(input())
for i in range(m,n+1):
    if ispalinedrome(i):
        print(i,end=" ")