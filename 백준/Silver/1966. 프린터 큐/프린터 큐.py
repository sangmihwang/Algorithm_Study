import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    pri = list(map(int, input().split()))
    for i in range(N):
        pri[i] = (i, pri[i])
    q = deque(pri)
    cnt = 1
    while q:
        maxP = 0
        for qq in q:
            if qq[1] >= maxP:
                maxP = qq[1]
        x = q.popleft()
        if x[1] == maxP:
            if x[0] == M:
                print(cnt)
                break
            else:
                cnt += 1
        else:
            q.append(x)