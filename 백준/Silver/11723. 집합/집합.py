import sys
input = sys.stdin.readline

M = int(input())
S = []
for _ in range(M):
    inp = list(map(str, input().strip().split()))
    if inp[0] == 'add':
        if int(inp[1]) not in S:
            S.append(int(inp[1]))
    elif inp[0] == 'check':
        if int(inp[1]) in S:
            print(1)
        else:
            print(0)
    elif inp[0] == 'remove':
        if int(inp[1]) in S:
            S.remove(int(inp[1]))
    elif inp[0] == 'toggle':
        if int(inp[1]) in S:
            S.remove(int(inp[1]))
        else:
            S.append(int(inp[1]))
    elif inp[0] == 'all':
        S = [i for i in range(1, 21)]
    elif inp[0] == 'empty':
        S = []
    
