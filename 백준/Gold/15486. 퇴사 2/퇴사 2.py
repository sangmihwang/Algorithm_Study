import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
for i in range(1, N+1):
    time, price = map(int, input().split())
    
    dp[i] = max(dp[i], dp[i-1])
    if 0 <= i + time - 1 <= N:
        dp[i+time-1] = max(dp[i-1]+price, dp[i+time-1])

print(max(dp))