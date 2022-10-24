from math import factorial
n = input()
sum = 0
for i in n:
    sum += factorial(int(i))
if sum == int(n):
    print("The number "+n+" is a strong number")
else:
    print("The number "+n+" is not a strong number")