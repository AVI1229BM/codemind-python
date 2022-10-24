n = input()
product = 1
sum = 0
for i in n:
    product *= int(i) 
for j in n:
    sum += int(j)
print(product-sum)
    
    