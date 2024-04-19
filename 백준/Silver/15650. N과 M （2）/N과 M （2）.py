import sys
input = sys.stdin.readline

def bt(tmp):
    if len(lst) == M:
        print(*lst)
        return
    if tmp > N:
        return
    lst.append(tmp)
    bt(tmp+1)
    lst.remove(tmp)
    bt(tmp+1)


N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
lst = []
ans = []
bt(1)
