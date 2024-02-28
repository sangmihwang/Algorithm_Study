import sys
input = sys.stdin.readline

def sol(mid):
    tmp, cnt = 0, 0
    for i in range(N):
        if tmp < exp[i]:    # 쓸 돈보다 현재 금액 부족하면
            tmp = mid      # 인출하고
            cnt += 1
            tmp -= exp[i] 
        else:               # 충분하면
            tmp -= exp[i]      # 지출
    return cnt


N, M = map(int, input().split())
exp = [int(input()) for _ in range(N)]
start, end = max(exp), sum(exp)
ans = 0
while start <= end:
    mid = (start + end) // 2
    if sol(mid) > M:        
        
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)