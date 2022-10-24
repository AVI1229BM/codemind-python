n = int(input())
m = int(input())
fsum = 0
ssum = 0
for i in range(1,int(n/2)+1):
    if n%i == 0:
        fsum += i
for i in range(1,int(m/2)+1):
    if m%i == 0:
        ssum += i
if n == ssum and m == fsum:
    print("Amicable")
else:
    print("Not Amicable")