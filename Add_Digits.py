n = input()
def su(n):
	sum = 0
	for i in n :
		sum +=int(i)
	if len(str(sum))<2:
		 return sum
	else:
		 return su(str(sum))
		 
print(su(n))