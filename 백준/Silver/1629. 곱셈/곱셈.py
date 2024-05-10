import sys
input = sys.stdin.readline

def sol(A, B, C):
    if B == 0:
        return 1
    if B % 2:
        return (sol(A, B//2, C) ** 2 * A ) % C
    else:
        return (sol(A, B//2, C) ** 2) % C

A, B, C = map(int, input().split())
# 곱셈의 나머지 법칙
# (A * B) % C = ((A % C) * (B % C)) % C

print(sol(A, B, C))