n = int(input())
if n*n == int((str(int((str(n)[::-1]))*int((str(n)[::-1])))[::-1])):
    print("True")
else:
    print("False")