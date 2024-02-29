import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n
tmp = 0

for i in range(n):
    tmp += nums[i]
    if tmp < 0 :
        tmp = 0
    else:
        dp[i] = tmp
# print(dp)
        
if dp == [0]*n:
    print(max(nums))
else:
    print(max(dp))