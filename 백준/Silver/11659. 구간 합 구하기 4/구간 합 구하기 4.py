import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums = [0] + nums
for i in range(1, N+1):
    nums[i] = nums[i-1]+nums[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(nums[j]-nums[i-1])