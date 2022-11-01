n=int(input())
sum=0
count=0
while n:
    s=n%10
    n=n//10
    sum=sum+s*s
    if n==0 and count<6 and (sum!=0 or sum!=7):
        n=sum
        sum=0
        count+=1
if sum==1 or sum==7:
    print(True)
else:
    print(False)