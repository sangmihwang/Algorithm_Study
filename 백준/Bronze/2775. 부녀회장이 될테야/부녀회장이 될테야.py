import sys
input = sys.stdin.readline

apt = [[0]*15 for _ in range(15)]
k = 0
while k <= 14:
    if k == 0:
        for n in range(15):
            apt[k][n] = n
    else:
        tmp = 0
        for n in range(1, 15):
            tmp += apt[k-1][n]
            apt[k][n] = tmp
    k += 1

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(apt[k][n])