n = int(input())
cnt = 0

for hour in range(0, n+1):
    for minute in range(0, 60):
        for second in range(0, 60):
            if '3' in [*list(str(hour)), *list(str(minute)), *list(str(second))]:
            # if '3' in str(hour)+str(minute)+str(second):
                cnt += 1
        
print(cnt)