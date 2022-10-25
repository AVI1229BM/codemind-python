n = int(input())
square = n*n
sum = 0
for i in str(square):
    sum+=int(i)
if sum == n:
    print("Neon Number")
else:
    print("Not Neon Number")