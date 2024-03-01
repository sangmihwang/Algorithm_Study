import sys
input = sys.stdin.readline
       

T = int(input())
for _ in range(T):
    N = int(input())
    dp = [0]*(N+1)
    for i in range(1, N+1):
        if i <= 3:
            dp[i] = 1
        elif i == 4:
            dp[i] = 2
        else:
            dp[i] = dp[i-5]+dp[i-1]
    print(dp[N])