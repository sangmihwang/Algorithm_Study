N, K = map(int, input().split())
coin = list(int(input()) for _ in range(N))

i = N - 1
cnt = 0
while K > 0:
    x = K // coin[i]
    if x > 0:
        cnt += x
        K -= coin[i]*x
    else:
        i -= 1
print(cnt)