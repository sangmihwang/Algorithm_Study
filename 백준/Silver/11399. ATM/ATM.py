import sys
input = sys.stdin.readline

N = int(input())
ppl = list(map(int, input().split()))
lst = []
for i in range(N):
    lst.append((i+1, ppl[i]))
lst.sort(key=lambda x: x[1])

tmp = 0
ans = 0
for i in range(N):
    tmp += lst[i][1]
    ans += tmp
print(ans)