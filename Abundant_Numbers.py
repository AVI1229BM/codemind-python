n = int(input())
h = 0
for i in range(1,int(n/2)+1):
    if n%i == 0:
      h += i   
if h > n:
    print("True")
else:
    print("False")