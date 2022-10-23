n = int(input())
def prefect(n):
   divisor = 0
   for i in range(1,int(n/2)+1):
       if n%i == 0:
          divisor += i
   return divisor
sum = prefect(n)
if sum == n:
    print("True")
else:
    print("False")
 