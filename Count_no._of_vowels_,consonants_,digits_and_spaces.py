n = input()
o = 0
c = 0
d = 0
w = 0
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        o += 1
    elif i == '0' or i ==  '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        d += 1
    elif i==" ":
        w+=1
    else:
        c += 1
print("Vowels:",o)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)