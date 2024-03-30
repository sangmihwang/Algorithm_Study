import sys
input = sys.stdin.readline
from collections import deque

def DFS(v):
    ansD.append(v)
    visitedD[v] = 1
    for i in range(1, N+1):
        if arr[v][i] and not visitedD[i]:
            DFS(i)
    else:
        return

def BFS(v):
    while d:
        x = d.popleft()
        for i in range(1, N+1):
            if x!= i and arr[x][i] and not visitedB[i]:
                d.append(i)
                ansB.append(i)
                visitedB[i] = 1
    
N, M, V = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
visitedD = [0]*(N+1)
visitedB = [0]*(N+1)
ansD = []
d = deque([V])
ansB = [V]
for _ in range(M):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1

DFS(V)
visitedB[V] = 1
BFS(V)

print(*ansD)
print(*ansB)