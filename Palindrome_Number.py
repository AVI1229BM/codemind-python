t = input()
c = 0
for i in range(int(t)):
    n = input()
    if n == n[::-1]:
      print("True")
    else:
        print("False")