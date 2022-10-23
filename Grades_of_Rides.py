a,b,c = map(int,input().split())
grade = 0
if a>50 and b>60 and c>100:
    grade=10
elif a>50 and b>60:
    grade=9
elif b>60 and c>100:
    grade=8
elif a>50 and c>100:
    grade = 7
elif a>50 or b>60 or c>100:
    grade = 6
else:
    grade=5
print(grade)