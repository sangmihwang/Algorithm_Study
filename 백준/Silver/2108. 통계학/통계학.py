import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
print(round(sum(nums)/N))
nums.sort()
print(nums[N//2])
numsD = {}
for n in nums:
    numsD[n] = numsD.get(n, 0) + 1
maxV = 0
ans = -5001
for k, v in numsD.items():
    if v > maxV:
        maxV = v
        ans = k
can = []
for k, v in numsD.items():
    if v == maxV:
        can.append(k)
if len(can) >= 2:
    print(can[1])
else:
    print(ans)
print(max(nums)-min(nums))