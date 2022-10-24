n = input()
square = int(n)*int(n)
digitsum = 0
for i in str(square):
    digitsum += int(i)
if int(n) == digitsum:
    print("Neon Number")
else:
    print("Not Neon Number")
    