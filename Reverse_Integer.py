t = str(input())
n = ""
for i in t:
    if i == '0':
        continue
    else:
        n+=i
if int(n)<0:
   m  = -int(n)
   c = str(m)+"-"
   print(str(c)[::-1])
else:
   print(n[::-1])
