import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dict = {}
    for _ in range(n):
        cloth, cate = map(str, input().strip().split())
        dict[cate] = dict.get(cate, [])
        dict[cate].append(cloth)
    ans = 1
    for d in dict:
        ans *= (len(dict[d])+1)
    print(ans-1)