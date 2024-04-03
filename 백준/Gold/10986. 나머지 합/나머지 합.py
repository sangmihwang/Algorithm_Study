import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

tmp = 0
rest = [0] * (N+1)
prefix = [0]*(N+1)
for i in range(1, N+1):
    rest[i] = nums[i] % M     # num을 M으로 나눈 나머지 리스트

for i in range(1, N+1):
    tmp = (tmp + rest[i]) % M   # 현재 값에 더하고 M으로 나눈 값
    rest[i] = tmp

reDict = {}
for r in rest:
    reDict[r] = reDict.get(r, 0) + 1
ans = 0
for k, v in reDict.items():
    if k == 0:
        ans += (v-1)
        ans += (v-1)*(v-2)//2
    else:
        ans += v*(v-1)//2
#     print(ans)
# print(reDict)
print(ans)