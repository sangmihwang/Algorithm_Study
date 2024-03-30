import sys
input = sys.stdin.readline


def DP(N):
    dp = [1]*(10000+1)
    for i in range(2, 10001):
        dp[i] += dp[i-2]
    for i in range(3, 10001):
        dp[i] += dp[i-3]
    return dp[N]

T = int(input())
for _ in range(T):
    n = int(input())
    print(DP(n))
