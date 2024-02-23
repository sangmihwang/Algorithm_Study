import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
for i in range(1, N+1):
    q.append(i)

if N == 1:
    print(1)
else:
    while True:
        q.popleft()
        if len(q) == 1:
            print(q[0])
            break
        x = q.popleft()
        q.append(x)
        if len(q) == 1:
            print(q[0])
            break