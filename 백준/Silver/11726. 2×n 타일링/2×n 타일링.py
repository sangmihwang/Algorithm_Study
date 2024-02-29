import sys
input = sys.stdin.readline

n = int(input())
lst = [0]*(n+1)

if n == 1:
    lst = [0, 1]
elif n == 2:
    lst = [0, 1, 2]
elif n > 2:
    lst[1] = 1
    lst[2] = 2
    for i in range(3, n+1):
        lst[i] = lst[i-2]+lst[i-1]

print(lst[n]%10007)
# 1 2 3 5 8 13 21 34 55