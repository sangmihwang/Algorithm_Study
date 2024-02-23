import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    inp = list(map(str, input().strip().split()))
    if inp[0] == 'push_front':
        q.appendleft(inp[1])
    elif inp[0] == 'push_back':
        q.append(inp[1])
    elif inp[0] == 'pop_front':
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif inp[0] == 'pop_back':
        if q:
            x = q.pop()
            print(x)
        else:
            print(-1)
    elif inp[0] == 'size':
        print(len(q))
    elif inp[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif inp[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif inp[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)