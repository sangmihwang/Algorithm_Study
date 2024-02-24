import sys
input = sys.stdin.readline

N = int(input())

# 몇번째 껍질인지 구하면 됨
ends = [1]
tmp = 1
i = 1
if N != 1:
    while tmp <= N:
        tmp += 6*i
        ends.append(tmp)
        i += 1

ans = 0
for e in range(len(ends)-1):
    if ends[e] < N <= ends[e+1]:
        ans = e + 1
print(ans+1)