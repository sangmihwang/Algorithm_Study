import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

if (V-A)%(A-B):
    day = int((V-A)//(A-B)) + 2
else:
    day = int((V-A)//(A-B)) + 1
print(day)