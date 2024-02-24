import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
cir = [i for i in range(1, N+1)]
ans = []
i = -1
while cir:
    i += K
    if i >= len(cir):
        i = i % len(cir)
        x = cir.pop(i)
        ans.append(x)
    else:
        y = cir.pop(i)
        ans.append(y)
    i -= 1

answer = '<'    
for i in range(len(ans)-1):
    answer += str(ans[i])+', '
answer += str(ans[-1]) +'>'
print(answer)