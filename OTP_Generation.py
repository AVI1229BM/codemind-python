n = input()
h = ""
for i in n:
    if int(i)%2==0:
        continue
    else:
     h += str(int(i)*int(i))
print(h)