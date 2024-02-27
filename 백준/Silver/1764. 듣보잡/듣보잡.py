import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mentioned = {}
ans = []
for _ in range(N+M):
    word = input().strip()
    if word not in mentioned:
        mentioned[word] = 1
    else:
        ans.append(word)
# neverHeard = [input().strip() for _ in range(N)]
# neverSeen = [input().strip() for _ in range(M)]

# ans = [x for x in neverHeard if x in neverSeen]
ans.sort()
print(len(ans))
for x in ans:
    print(x)