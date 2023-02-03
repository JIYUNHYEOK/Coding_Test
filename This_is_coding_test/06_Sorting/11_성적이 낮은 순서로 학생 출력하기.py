# 6-11 성적이 낮은 순서로 학생 출력하기

n = int(input())
grade_dict = {}
for _ in range(n):
    info = input().split()
    grade_dict.setdefault(info[0], info[1])

grade_dict = sorted(grade_dict.items(), key=lambda x: x[1])
print(*[i[0] for i in grade_dict])

##################################################################
n = int(input())
arr = []
for _ in range(n):
    info = input().split()
    arr.setdefault(info[0], info[1])

arr = sorted(arr, key=lambda x: x[1])

for student in arr:
    print(student[0], end = ' ')