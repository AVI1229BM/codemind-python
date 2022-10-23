n = int(input())
asci = 64
for i in range(n,0,-1):
    for j in range(i):
        print(chr(asci+i),end=" ")
    print()