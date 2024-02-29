import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

def sol(start, end):
    tmp = 0
    for i in range(N):
        if tree[i] > mid:
            tmp += (tree[i] - mid)
    return tmp

i, j = 0, max(tree)
while i <= j:
    mid = (i+j) // 2
    if sol(i, j) < M:
        j = mid - 1
    else:
        ans = mid
        i = mid + 1
    
print(ans)
    