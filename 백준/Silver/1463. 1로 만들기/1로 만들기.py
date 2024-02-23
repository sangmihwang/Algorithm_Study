N = int(input())

dp = [float('inf')]*1000001
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, N+1):
    can = []
    if not i%2:
        can.append(dp[i//2] + 1)
    if not i%3:
        can.append(dp[i//3] + 1)
    can.append(dp[i-1] + 1)
    dp[i] = min(can)
# print(dp)
print(dp[N])