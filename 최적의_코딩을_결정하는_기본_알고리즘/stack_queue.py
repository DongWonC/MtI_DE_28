'''
# 스택 구현 예제(Python)
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])  # 최상단 원소부터 출력
print(stack)    # 최하단 원소부터 출력
'''
'''
# 큐 구현 예제(Python)
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()    # 5
queue.append(1)
queue.append(4)
queue.popleft()    # 2

print(queue)    # 먼저 들어온 순서대로 출력 (3, 7, 1, 4)
queue.reverse() # 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력 (4, 1, 7, 4)
'''

