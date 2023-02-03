from collections import deque

queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# 먼저 들어온 순서대로 출력
print(queue)

# 다음 출력을 위해 역순으로 바꾸기
queue.reverse()

# 나중에 들어온 원소부터 출력
print(queue)