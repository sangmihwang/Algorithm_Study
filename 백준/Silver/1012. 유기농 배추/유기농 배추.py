import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def sol(x, y):
    visited[x][y] = 1
    for i in range(4):
        canX, canY = x+dx[i], y+dy[i]
        if isInrange(canX, canY) and not visited[canX][canY] and arr[canX][canY]:
            sol(canX, canY)
    else:
        return
    
def isInrange(i, j):
    if 0 <= i <= N-1 and 0<= j <= M-1:
        return True
    
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                cnt += 1
                sol(i, j)
    print(cnt)