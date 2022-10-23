n = int(input())
ch = 'A'
for i in range(n):
  for j in range(n):
    print(ch,end=" ")
  print()
  ch = chr(ord(ch)+1)