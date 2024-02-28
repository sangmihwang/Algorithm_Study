import sys
input = sys.stdin.readline

def sol(N, tmp):
    global cnt
    if tmp == N:
        cnt += 1
        return
    elif tmp > N:
        return
    sol(N, tmp+1)
    sol(N, tmp+2)
    sol(N, tmp+3)


T = int(input())
for _ in range(T):
    target = int(input())
    cnt = 0
    sol(target, 0)
    print(cnt)