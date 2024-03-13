import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sbn = [0] + list(map(int, input().split()))
# [0, -1, 1, 2, 3, 3]: 1번은 사장, 2번의 직속 상사는 1번(sbn[2]), 3번의 직속 상사는 2번(sbn[3])
com = [0]*(n+1)                   # 칭찬 받은 수치 리스트

for _ in range(m):
    employee, w = map(int, input().split())            # 칭찬 목록
    com[employee] += w
# print(com)
ans = [0]*(n+1) 
for i in range(1, n+1):
    if sbn[i] == -1:
        continue
    else:
        com[i] += com[sbn[i]]
    # print(com)
print(*com[1:])