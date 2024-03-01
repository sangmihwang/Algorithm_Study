import sys
input = sys.stdin.readline

N = int(input())
lst = [0]*(N+1)

if N == 1:
    lst = [0, 1]
elif N == 2:
    lst = [0, 1, 3]
else:
    lst[1] = 1
    lst[2] = 3
    for i in range(3, N+1):
        lst[i] = lst[i-1] + lst[i-2]*2

print(lst[N]%10007)